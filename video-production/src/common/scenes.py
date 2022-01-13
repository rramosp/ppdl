import logging
logger = logging.getLogger('matplotlib')
logger.setLevel(logging.INFO)

from manim import *
from common.objects import *
from common.utils import *
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
    course_title = "Probabilistic Programming in Practice"
    course_subtitle = "Bayesian Statistics - Deep Learning - Tensorflow Probability"
    t1 = Text(course_title, color=BLACK, 
              font="sans-serif", font_size=48).shift(UP*2)
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
                               .move_to([-5.7,-3.5,0])

    logo_udea = get_imgmobject("logo-std-udea-ingenieria").scale(0.5)\
                               .move_to([-1.5,-3,0])
    logo_unal = get_imgmobject("logo-std-unal").scale(0.5).next_to(logo_udea, RIGHT)

    t4 = Text("sponsored by", color=BLACK, font="sans-serif", font_size=12)\
              .move_to([4.5,-3.5, 0])
    logo_google = get_imgmobject("logo-std-google").scale(0.3).next_to(t4, RIGHT)

    scene.add_sound(find_soundfile("intro"))
    scene.play(FadeIn(t1), FadeIn(t2))
    scene.play(Write(t3), FadeIn(l)) 
    scene.play(FadeIn(logo_udea), FadeIn(logo_unal))
    scene.play(FadeIn(t4), FadeIn(logo_google), FadeIn(logo_tf))
    scene.wait(1)
    scene.play(FadeOut(t1),FadeOut(t2), FadeOut(logo_udea), FadeOut(logo_unal),
               FadeOut(t4), FadeOut(logo_google), FadeOut(logo_tf), FadeOut(l))
    #scene.wait(1)
    scene.play(FadeOut(t3))
    scene.wait(2)



