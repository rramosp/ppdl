import logging
import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
from scipy import stats
import matplotlib.pyplot as plt


def play_joint(scene):
    from scipy.integrate import quad, dblquad
    import matplotlib
    matplotlib.rcParams.update({'font.size': 18})

    p_w = lambda w: 1.
    p_w = lambda w: stats.norm(loc=.7,scale=.1).pdf(w)
    p_w = lambda w: stats.beta(3,2).pdf(w)
    p_conditional = np.vectorize(lambda l,w: stats.norm(loc=2+w**2, scale=.2+w/2).pdf(l))
    p_lw = np.vectorize(lambda l,w: p_conditional(l,w)*p_w(w))

    lr = np.linspace(0,5,100)
    wr = np.linspace(0,1,100)
    L,W = np.meshgrid(lr,wr)
    Z = p_lw(L,W)    

    fig = plt.figure(figsize=(10,8))
    cp = plt.contourf(W, L, Z, cmap=plt.cm.Blues)
    plt.colorbar(cp)
    plt.xlabel("width")
    plt.ylabel("length")

    mo = get_matplotlibfig(fig).move_to([1,-1,0])
    scene.play(FadeIn(mo))
    scene.wait(1)

    h  = mo.get_top() - mo.get_bottom()
    w  = mo.get_right() - mo.get_left()
    bl = mo.get_bottom() + h*.11  -w*0.375
    br = mo.get_bottom() + h*.11  +w*0.245
    tl = mo.get_bottom() + h*.878 -w*0.375
    tr = mo.get_bottom() + h*.878 +w*0.245
    lv  = Line(bl, tl)
 
    lg = get_axes(xmin=1, xmax=4,
                  ymin=0, ymax=2, 
                  x_length=3, y_length=1,
                  x_splits=7, y_splits=0,
                  xlabel="length", 
                  xlabel_kwargs={'font_size': 24},
                  additional_x_axis_config={'decimal_number_config' : {'color': '#222222','num_decimal_places': 1 }}

                  ).move_to([-5,-2,0])

    lplane = lg[0]
    ltitle = MathTex(r"\text{conditional probability } P(l|w=", font_size=24).next_to(lplane,UP)
    ltitle_wvalue = DecimalNumber(num_decimal_places=2, font_size=24).set_color(BLACK).next_to(ltitle,.2*RIGHT)
    ltitle2 = MathTex(r")", font_size=24).next_to(ltitle_wvalue,.2*RIGHT)
    vtitle = VGroup(ltitle, ltitle_wvalue, ltitle2)

    ltf = TransformFunction(lplane, lambda w: np.vectorize(lambda l: p_conditional(l,w)), 0, 1)
    ltf.function_graph.set_color(BLUE_C)

    lcc = CountAnimation(ltitle_wvalue,0,1)

    scene.play(FadeIn(lg), FadeIn(ltf.function_graph), FadeIn(vtitle), FadeIn(lv))
    scene.wait(1)
    scene.play(lv.animate.move_to(lv.get_center() + (br - bl)), ltf, lcc, run_time=3)

    scene.wait(1)
    ltf.switch_direction()
    lcc.switch_direction()
    scene.play(lv.animate.move_to(lv.get_center() - (br - bl)), ltf, lcc, run_time=3)

    ltitle.set_value
    scene.wait(3)


class Main(Scene):
    def construct(self):

        #play_func(self)
        play_joint(self)


        self.wait(5)
        #play_credits(self)
        #self.wait(5)


        return