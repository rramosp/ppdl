import logging
logger = logging.getLogger('matplotlib')
logger.setLevel(logging.INFO)

from manim import *
from .objects import *
from .utils import *
import pandas as pd
class SceneTimer:
    """
    keeps time and prints out in the scene the elapsed time
    """
    def __init__(self, scene, debug_wait=False):
        self.debug_wait = debug_wait
        self.scene = scene
        self.text = Text("")
        self.ref = 0

    def reset(self):
        self.ref = self.scene.renderer.time
        return self

    def display_time(self, prefix=""):
        self.scene.remove(self.text)

        self.text = Text(f"{prefix}@{self.scene.renderer.time-self.ref:.3f} secs", 
                         font_size=20).to_edge(DR) 

        self.scene.add(self.text)

    def wait_until(self, nsecs):
        """
        waits until 'nsecs' of scene have passed.
        if 'nsecs' have already passed, no waiting happens
        nsecs: int with number of secs
               or string for pandas Timedelta, i.e. "3min 20sec"
        """

        if type(nsecs)==str:
            nsecs = pd.Timedelta(nsecs).seconds

        if self.debug_wait:
            s = f"wait till {nsecs} secs, "
            if self.ref>0:
                s += f"(+{self.ref:.1f} secs), "
            self.display_time(s)

        lapse = nsecs - (self.scene.renderer.time - self.ref)
        if lapse>0:
            self.scene.wait(lapse)
        if self.debug_wait:
            self.display_time("done ")


def play_intro_scene(scene, video_name):
    course_title = "Probabilistic Programming for Deep Learning"
    course_subtitle = "Bayesian Statistics - Deep Learning - Tensorflow Probability"
    t1 = Text(course_title, color=BLACK, 
              font="sans-serif", font_size=40).shift(UP*2)
    t2 = Text(course_subtitle, color=GRAY_C, 
              font_size=24, font="sans-serif").next_to(t1, DOWN)

    l = Line([-5,0,0], [5,0,0], color=GRAY_C, stroke_width=0.5).next_to(t2, 2*DOWN)

    video_names = [i for i in video_name.split("\n") if len(i.strip())!=0]

    m = 2
    t3 = VGroup()
    prev = l
    for t in video_names:
        t = Tex(t, color=BLUE_E, font_size=52).next_to(prev, m*DOWN)
        t3.add(t)
        m = 1
        prev = t

    logo_tf = get_imgmobject("logo-std-tf").scale(0.5)\
                               .move_to([6,-3.5,0])

    logo_udea = get_imgmobject("logo-std-udea-ingenieria").scale(0.5)\
                               .move_to([-1.8,-3,0])
    logo_unal = get_imgmobject("logo-std-unal").scale(0.5).next_to(logo_udea, RIGHT*5)

    t4 = Text("sponsored by", color=BLACK, font="sans-serif", font_size=12)\
              .move_to([6,-3.2, 0])
    #logo_google = get_imgmobject("logo-std-google").scale(0.3).next_to(t4, RIGHT)

    scene.add_sound(find_soundfile("intro-salsa"))
    scene.play(FadeIn(t1), FadeIn(t2), FadeIn(logo_udea), FadeIn(logo_unal), FadeIn(t4), FadeIn(logo_tf))
    scene.play(Write(t3), FadeIn(l)) 
    scene.wait(2)
    scene.play(FadeOut(t1),FadeOut(t2), FadeOut(logo_udea), FadeOut(logo_unal),
               FadeOut(t4), FadeOut(logo_tf), FadeOut(l))
    scene.wait(1)
    scene.play(FadeOut(t3))
    scene.wait(1)

def play_credits(scene):
    scene.clear()
    t0 = Text(r"Probabilistic Programming for Deep Learning", font_size=36, color=BLUE_E).move_to([-0.5,2.5,0])
    t1 = MathTex(r"\text{Course design}", color=BLACK).next_to(t0, DOWN*1.5).align_to(t0, LEFT)
    t2a  = MathTex(r"\text{Raúl Ramos}", color=BLUE_E, font_size=36).next_to(t1, DOWN).align_to(t1, LEFT)
    t2aa = MathTex(r"\text{Universidad de Antioquia}", color=RED_C, font_size=24).next_to(t2a, RIGHT)
    t2b = MathTex(r"\text{Fabio González}", color=BLUE_E, font_size=36).next_to(t2a, DOWN).align_to(t2a, LEFT)
    t2bb = MathTex(r"\text{Universidad Nacional de Colombia}", color=RED_C, font_size=24).next_to(t2b, RIGHT)

    t3 = MathTex(r"\text{With the collaboration of}").move_to([0,2,0]).next_to(t2b, DOWN*2).align_to(t2b, LEFT)
    t4 = MathTex(r"\text{Felipe Ángel}", color=BLUE_E, font_size=36).next_to(t3, DOWN).align_to(t3, LEFT)
    t4a = MathTex(r"\text{animations}", color=RED_C, font_size=24).next_to(t4, RIGHT)
    t5 = MathTex(r"\text{Sebastián Lara}", color=BLUE_E, font_size=36).next_to(t4, DOWN).align_to(t4, LEFT)
    t5a = MathTex(r"\text{graders and notebooks}", color=RED_C, font_size=24).next_to(t5, RIGHT)

    logo_tf = get_imgmobject("logo-std-tf").scale(0.5)\
                               .move_to([6,-3.5,0])

    logo_udea = get_imgmobject("logo-std-udea-ingenieria").scale(0.5)\
                               .move_to([-1.8,-3,0])
    logo_unal = get_imgmobject("logo-std-unal").scale(0.5).next_to(logo_udea, RIGHT*5)
    sponsored = Text("sponsored by", color=BLACK, font="sans-serif", font_size=12)\
              .move_to([6,-3.2, 0])

    g1 = VGroup(t0,t1,t2a,t2b,t3,t4,t4a, t5, t5a, t2aa, t2bb)
    g2 = Group(logo_udea, logo_unal, logo_tf, sponsored)

    scene.play(Write(g1), FadeIn(g2))


def play_continuous_function(
        scene, 
        fun, 
        xmin, 
        xmax, 
        position, 
        title = "", 
        transform_from = None,
        additional_x_axis_config={},
        additional_y_axis_config={},
        animation_run_time=0,
        x_splits = 4
    ):

    g = graph_function(
        fun = fun, 
        xmin = xmin, 
        xmax = xmax, 
        title = title, 
        additional_x_axis_config = additional_x_axis_config,
        additional_y_axis_config = additional_y_axis_config,
        x_splits = x_splits
    )    

    g = g.move_to(position)
    axes, graph = g[0], g[1]

    def moving_line():
        f = graph.underlying_function
        l = Line(
                start = axes.c2p(tracker.get_value(), 0), 
                end=axes.c2p(tracker.get_value(), f(tracker.get_value())), 
                stroke_width=1
            )
        d = Dot(axes.c2p(tracker.get_value(), 0), color=BLACK, radius=0.05)
        t = Text(f"{tracker.get_value():.1f}", font_size=12).next_to(d, DOWN*2)
        g = VGroup(l, d, t)
        return g


    self = scene
    if transform_from is None:
        self.play(Create(g))
    else:
        self.play(Transform(transform_from, g))

    if animation_run_time>0:
        tracker = ValueTracker(xmin)
        redraw_line = always_redraw(moving_line)
        self.add(redraw_line)
        self.play(tracker.animate.set_value(xmax), rate_func=smooth, run_time=animation_run_time/2)

        tracker = ValueTracker(xmax)
        self.play(tracker.animate.set_value(xmin), rate_func=smooth, run_time=animation_run_time/2)
        scene.remove(redraw_line)

    return g


def play_wheely_bye(scene, position=[0,0,0]):
    w = Wheely(mode="smile").scale(0.3).move_to(position)
    scene.play(FadeIn(w))
    scene.wait(10)
    scene.play(*w.rotate_wheel(), *w.change_mode("thinking"))

    return w
