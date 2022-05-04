import logging
import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


def play_joint(scene):
    from scipy.integrate import quad, dblquad
    import matplotlib
    matplotlib.rcParams.update({'font.size': 18})

    joint = MathTex(r"\text{Joint distribution    } P(l,w)").to_edge(UP)

    condition_1 = MathTex(r"\int_0^5 \int_0^1 P(l,w)\text{d}w \text{d}l = 1", font_size=20).next_to(joint, DOWN).shift(LEFT*3)
    condition_2 = MathTex(r"\int_C P(l,w)\text{d}C \in (0,1)", font_size=20).next_to(condition_1, RIGHT*3)
    condition_2a = MathTex(r"\text{ with }C\text{ any 2D area in the }(l,w)\text{ plane}", font_size=20).next_to(condition_2, RIGHT*2)

    f = np.vectorize(lambda l,w: np.exp(-(w*4+l/10-2)**2) * (np.exp(-(l*2-1-5*w)**2) + np.exp(-(w+l-3.5)**2)))
    nZ = dblquad(f, 0,1, lambda k: 0, lambda k: 5)[0]
    p_lw = np.vectorize(lambda l,w: np.exp(-(w*4+l/10-2)**2) * (np.exp(-(l*2-1-5*w)**2) + np.exp(-(w+l-3.5)**2)) / nZ)

    @np.vectorize
    def p_l_given_w(l,w):
        nZ = quad(lambda l: p_lw(l,w), 0,5)[0]
        return p_lw(l,w)/nZ

    @np.vectorize
    def p_w_given_l(l,w):
        nZ = quad(lambda w: p_lw(l,w), 0,1)[0]
        return p_lw(l,w)/nZ


    sqx = Rectangle(width=3.4, height=1, fill_opacity=1, color=WHITE, fill_color=WHITE).move_to([1,1.95,0])
    sqy = Rectangle(width=1, height=3.6, fill_opacity=1, color=WHITE, fill_color=WHITE).move_to([2.95,0,0])
    scene.add_foreground_mobjects(sqx)
    scene.add_foreground_mobjects(sqy)

    lr = np.linspace(0,5,100)
    wr = np.linspace(0,1,100)
    L,W = np.meshgrid(lr,wr)
    Z = p_lw(L,W)

    # definitions for the axes
    g = sns.JointGrid(height=6)
    cp = g.ax_joint.contourf(W, L, Z, cmap=plt.cm.Blues)
    g.ax_marg_x.plot(wr, Z.sum(axis=1))
    g.ax_marg_y.plot(Z.sum(axis=0), lr)
    g.ax_joint.set_xlabel("width")
    g.ax_joint.set_ylabel("length")
    #cbar_ax = g.fig.add_axes([-.1, .05, .02, .77])
    #plt.colorbar(cp, cax=cbar_ax)

    mo = get_matplotlibfig(g.fig).move_to([1,0,0])
    scene.play(FadeIn(mo), FadeIn(joint))
    scene.wait(1)
    scene.play(FadeIn(condition_1))
    scene.wait(1)
    scene.play(FadeIn(condition_2), FadeIn(condition_2a))

    scene.wait(3)
    scene.play(FadeOut(condition_1), FadeOut(condition_2), FadeOut(condition_2a))

    # marginal for w
    fw = MathTex(r"P(w) = \int_0^5 P(l,w)\text{d}l", font_size=20).move_to([1,2.5,0])
    scene.play(FadeOut(sqx), FadeIn(fw))
    scene.wait(2)
    scene.play(FadeIn(sqx), FadeOut(fw))

    # marginal for l
    fl = MathTex(r"P(l) = \int_0^1 P(l,w)\text{d}w", font_size=20).move_to([4,0,0])
    scene.play(FadeOut(sqy), FadeIn(fl))
    scene.wait(2)
    scene.play(FadeIn(sqy), FadeOut(fl))
    scene.wait(2)


    h  = mo.get_top() - mo.get_bottom()
    w  = mo.get_right() - mo.get_left()
    bl = mo.get_bottom() + h*.10  -w*0.375
    br = mo.get_bottom() + h*.10  +w*0.315
    tl = mo.get_bottom() + h*.81  -w*0.375
    tr = mo.get_bottom() + h*.81  +w*0.315   
 
    # conditional P(l|w)
    wlg = get_axes(xmin=0, xmax=5,
                  ymin=0, ymax=.5, 
                  x_length=3, y_length=1,
                  x_splits=7, y_splits=0,
                  xlabel="length", 
                  xlabel_kwargs={'font_size': 24},
                  additional_x_axis_config={'decimal_number_config' : {'color': '#222222','num_decimal_places': 1 }}

                  ).move_to([-4,-1,0])
    wlv  = Line(bl, tl)

    wlplane = wlg[0]
    wltitle = MathTex(r"\text{conditional probability } P(l|w=", font_size=24).next_to(wlplane,UP)
    wltitle_value = DecimalNumber(num_decimal_places=2, font_size=24).set_color(BLACK).next_to(wltitle,.2*RIGHT)
    wltitle2 = MathTex(r")", font_size=24).next_to(wltitle_value,.2*RIGHT)
    wvtitle = VGroup(wltitle, wltitle_value, wltitle2)

    wltf = TransformFunction(wlplane, lambda w: np.vectorize(lambda l: p_l_given_w(l,w)), 0, 1)
    wltf.function_graph.set_color(BLUE_C)

    wlcc = CountAnimation(wltitle_value,0,1)

    scene.play(FadeIn(wlg), FadeIn(wltf.function_graph), FadeIn(wvtitle), FadeIn(wlv))
    scene.wait(1)
    scene.play(wlv.animate.move_to(wlv.get_center() + (br - bl)), wltf, wlcc, run_time=3)

    scene.wait(1)
    wltf.switch_direction()
    wlcc.switch_direction()
    scene.play(wlv.animate.move_to(wlv.get_center() - (br - bl)), wltf, wlcc, run_time=3)

    scene.wait(1)
    scene.play(FadeOut(VGroup(wlv, wvtitle, wlplane, wlg, wltf.function_graph)))


    # conditional P(w|l)
    llg = get_axes(xmin=0, xmax=1,
                  ymin=0, ymax=.5, 
                  x_length=3, y_length=1,
                  x_splits=7, y_splits=0,
                  xlabel="width", 
                  xlabel_kwargs={'font_size': 24},
                  additional_x_axis_config={'decimal_number_config' : {'color': '#222222','num_decimal_places': 1 }}

                  ).move_to([-4,-1,0])

    llv  = Line(bl, br)

    llplane = llg[0]
    lltitle = MathTex(r"\text{conditional probability } P(w|l=", font_size=24).next_to(llplane,UP)
    lltitle_value = DecimalNumber(num_decimal_places=2, font_size=24).set_color(BLACK).next_to(lltitle,.2*RIGHT)
    lltitle2 = MathTex(r")", font_size=24).next_to(lltitle_value,.2*RIGHT)
    lvtitle = VGroup(lltitle, lltitle_value, lltitle2)

    lltf = TransformFunction(llplane, lambda l: np.vectorize(lambda w: p_w_given_l(l,w)), 0, 5)
    lltf.function_graph.set_color(BLUE_C)

    llcc = CountAnimation(lltitle_value,0,5)

    scene.play(FadeIn(llg), FadeIn(lltf.function_graph), FadeIn(lvtitle), FadeIn(llv))
    scene.wait(1)
    scene.play(llv.animate.move_to(llv.get_center() + (tl - bl)), lltf, llcc, run_time=3)

    scene.wait(1)
    lltf.switch_direction()
    llcc.switch_direction()
    scene.play(llv.animate.move_to(llv.get_center() - (tl - bl)), lltf, llcc, run_time=3)



class Main(Scene):
    def construct(self):

        #play_func(self)
        play_joint(self)


        self.wait(5)
        #play_credits(self)
        #self.wait(5)


        return