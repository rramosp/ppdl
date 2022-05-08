import logging
import os, sys

from sympy import Ellipse

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

    timer = SceneTimer(scene,debug_wait=False).reset()


    t0 = MathTex(r"\text{Discrete } \rightarrow \text{ continuous}").shift(UP*2)
    t1 = MathTex(r"\sum \rightarrow \int").next_to(t0, DOWN)
    t2 = MathTex(r"\text{length} \in (0m,5m) \rightarrow \int_0^5").next_to(t1, DOWN)

    scene.play(Write(t0))
    timer.wait_until(16)
    scene.play(Write(t1))
    timer.wait_until(20)
    scene.play(Write(t2))
    timer.wait_until(41)
    scene.play(FadeOut(t0,t1,t2))

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
    pc = Arrow(start=[0.,-1.3,0], end=[0.9,-.6,0], stroke_width=12, color="red")
    mo = get_matplotlibfig(g.fig).move_to([1,0,0])

    h  = mo.get_top() - mo.get_bottom()
    w  = mo.get_right() - mo.get_left()
    bl = mo.get_bottom() + h*.10  -w*0.375
    br = mo.get_bottom() + h*.10  +w*0.315
    tl = mo.get_bottom() + h*.81  -w*0.375
    tr = mo.get_bottom() + h*.81  +w*0.315   

    scene.play(FadeIn(mo))

    timer.wait_until("1min 30sec")
    scene.play(FadeIn(pc))
    timer.wait_until("1min 36sec")
    scene.play(pc.animate.shift(LEFT*.3 + UP*.8))
    timer.wait_until("1min 39sec")
    scene.play(pc.animate.shift(LEFT*.8 + DOWN*.8), runtime=3)
    timer.wait_until("1min 51sec")
    scene.play(FadeOut(pc))
    scene.play(FadeIn(joint))
    
    timer.wait_until("2min 6sec")
    scene.play(FadeIn(condition_1))
    timer.wait_until("2min 12sec")
    scene.play(FadeIn(condition_2), FadeIn(condition_2a))


    s1 = Circle(radius=.3, color="black", fill_opacity=.5).move_to([1.2,-.6,0])
    s1 = VGroup(s1,MathTex("C").next_to(s1))
    s2 = Ellipse(.3,0.8, color="black", fill_opacity=.5).shift(LEFT*.3+DOWN)
    s2 = VGroup(s2,MathTex("C").next_to(s2))
    s3 = RegularPolygon(4, radius=.5, color="black", fill_opacity=.5).shift(RIGHT*.5+UP*.5)
    s3 = VGroup(s3,MathTex("C").next_to(s3))

    timer.wait_until("2min 25sec")
    scene.play(FadeIn(s1), run_time=2)
    scene.wait(1)
    scene.play(Transform(s1,s2), run_time=2)
    scene.wait(1)
    scene.play(Transform(s1,s3), run_time=2)
    scene.wait(2)
    scene.play(FadeOut(s1))
    scene.wait(3)
    scene.play(FadeOut(condition_1), FadeOut(condition_2), FadeOut(condition_2a))

    # marginal for w
    fw = MathTex(r"P(w) = \int_0^5 P(l,w)\text{d}l", font_size=20).move_to([1,2.5,0])
    fl = MathTex(r"P(l) = \int_0^1 P(l,w)\text{d}w", font_size=20).move_to([4,0,0])

    timer.wait_until("2min 38sec")
    scene.play(FadeOut(sqy))
    timer.wait_until("2min 44sec")
    scene.play(FadeIn(sqy), FadeOut(sqx))
    timer.wait_until("2min 51sec")
    scene.play(FadeOut(sqx), FadeOut(sqy))

    timer.wait_until("2min 58sec")
    scene.play(FadeIn(fw), FadeIn(fl))


    timer.wait_until("3min 15sec")
    scene.play(Indicate(fw, color=BLACK, scale_factor=2), run_time=3)
    timer.wait_until("3min 30sec")
    scene.play(Indicate(fl, color=BLACK, scale_factor=2), run_time=2)

    timer.wait_until("3min 38sec")
    scene.play(FadeOut(fl, fw), FadeIn(sqy, sqx))
 
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

    timer.wait_until("3min 42sec")
    scene.play(FadeIn(wlg), FadeIn(wltf.function_graph), FadeIn(wvtitle), FadeIn(wlv))

    timer.wait_until("4min 02sec")
    scene.play(wlv.animate.move_to(wlv.get_center() + (br - bl)), wltf, wlcc, run_time=3)
    scene.wait(2)
    wltf.switch_direction()
    wlcc.switch_direction()
    scene.play(wlv.animate.move_to(wlv.get_center() - (br - bl)), wltf, wlcc, run_time=3)
    timer.wait_until("4min 20sec")
    wltf.switch_direction()
    wlcc.switch_direction()
    scene.play(wlv.animate.move_to(wlv.get_center() + (br - bl)*0.6), wltf, CountAnimation(wltitle_value,0,0.6), run_time=3)

    timer.wait_until("4min 40sec")
    wtext = MathTex(r"P(l|w=0.6)=\frac{P(l,w=0.6)}{P(w=0.6)}", font_size=30).next_to(wlplane, DOWN*3).shift(RIGHT)
    scene.play(Write(wtext))

    # conditional P(w|l)
    llg = get_axes(xmin=0, xmax=1,
                  ymin=0, ymax=3, 
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

    timer.wait_until("4min 48sec")
    scene.play(FadeOut(wlv, wvtitle, wlplane, wlg, wltf.function_graph, wtext))
    timer.wait_until("4min 50sec")
    scene.play(FadeIn(llg), FadeIn(lltf.function_graph), FadeIn(lvtitle), FadeIn(llv))
    scene.wait(1)
    scene.play(llv.animate.move_to(llv.get_center() + (tl - bl)), lltf, llcc, run_time=3)
    lltf.switch_direction()
    llcc.switch_direction()
    scene.play(llv.animate.move_to(llv.get_center() - (tl - bl)), lltf, llcc, run_time=3)

    scene.wait(1)
    ltext = MathTex(r"P(w|l)=\frac{P(l,w)}{P(l)}", font_size=30).next_to(wlplane, DOWN*3)
    scene.play(Write(ltext))

    timer.wait_until("5min 7sec")
    scene.play(FadeOut(llv, lvtitle, llplane, llg, lltf.function_graph, ltext))

    timer.wait_until("5min 15sec")
    plw05 = MathTex("P(w|l=2.5)").move_to([-4,-.15,0])
    parrow = Arrow(start=[0,0,0], end=[2,0,0], stroke_width=3, color="red").next_to(plw05, RIGHT)
    plw   = MathTex("P(w|l)").next_to(plw05, DOWN*0)
    plww   = MathTex(r"\text{unspecified }l", font_size=25, color=RED_E).next_to(plw, RIGHT)
    plwb   = Brace(mo, direction = [-1,0,0], color=RED_E).next_to(mo, LEFT).scale(0.7).shift(DOWN*.2)
    llv  = Line(bl+UP*1.6, br+UP*1.6)

    scene.play(Write(plw05), FadeIn(llv, parrow))
    timer.wait_until("5min 25sec")
    scene.play(FadeOut(plw05, llv, parrow))
    scene.wait(1)
    scene.play(FadeIn(plw, plww, plwb))
  
    timer.wait_until("5min 50sec")
    scene.play(FadeOut(plw, plww, plwb))


    text1 = MathTex(r"\text{joint distribution } P(l,w)").move_to([-4,1,0])
    text11 = MathTex(r"\text{full information}", font_size=25, color=BLUE_E).next_to(text1, DOWN*.5).shift(RIGHT*0)

    text2 = MathTex(r"\text{marginal distributions } P(l)\text{, } P(w)").next_to(text1, DOWN*3).align_to(text1, LEFT)
    text21 = MathTex(r"\text{an aggregation on the joint distribution}", font_size=25, color=BLUE_E).next_to(text2, DOWN*.5).align_to(text11, LEFT)

    text3 = MathTex(r"\text{conditional distributions } P(l|w)\text{, } P(w|l)").next_to(text2, DOWN*3).align_to(text2, LEFT)
    text31 = MathTex(r"\text{a }normalized\text{ cut on the joint distribution}", font_size=25, color=BLUE_E).next_to(text3, DOWN*.5).align_to(text21, LEFT)

    timer.wait_until("5min 52sec")
    scene.play(mo.animate.shift(RIGHT*2), sqx.animate.shift(RIGHT*2), sqy.animate.shift(RIGHT*2))
    scene.play(Write(text1), Write(text11))

    timer.wait_until("6min 02sec")
    scene.play(Write(text2), Write(text21), FadeOut(sqx), FadeOut(sqy))

    timer.wait_until("6min 15sec")
    scene.play(Write(text3), Write(text31), FadeIn(llv.shift(RIGHT*2)))


    timer.wait_until("6min 30sec")
    text4 = MathTex(r"P(l|w)=\frac{P(l,w)}{P(w)} \hspace{0.5cm} P(w|l)=\frac{P(l,w)}{P(l)}", font_size=30).next_to(text31, DOWN*2).align_to(text1, LEFT)
    scene.play(Write(text4))
    scene.wait(5)

class Main(Scene):
    def construct(self):

        video_name = r"marginals and conditionals for continuous distributions"
        play_intro_scene(self,video_name)
        self.wait(1)        
        
        sfile = find_soundfile("02.02-anim-05-ES") 
        self.add_sound(sfile)
        play_joint(self)

        play_credits(self)
        self.wait(5)

        return