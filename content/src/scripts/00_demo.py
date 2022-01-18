import logging
import os, sys
sys.path.insert(0, "src")

from manim import *
from common.scenes import *

def play_demo_scene(scene):
    f1 = Wheely(mode="scared").scale(0.3)
    t = TextCallout("adios bye\nbye adios").next_to(f1, UL, buff=0.)

    scene.add(f1)
    scene.play(*f1.rotate_wheel())
    scene.play(*t.show())
    f1.play_change_mode(scene, "thinking")
    
    scene.wait(3)
    scene.play(FadeOut(t))
    scene.play(ScaleInPlace(f1,0.5))
    scene.play(ApplyMethod(f1.move_to, Dot([-6,-3,0])))

    t = TextCallout("algo màs que pensé", direction=DL).next_to(f1, UR, buff=0.)
    scene.play(*t.show())
    scene.wait(2)
    f1.play_change_mode(scene, "smile")
    scene.play(FadeOut(t))
    scene.wait(2)

    t = MathTexCallout(r"\int_a^b f'(x) dx = f(b)- f(a)", direction=LEFT)\
                       .next_to(f1, RIGHT, buff=0.1)
    scene.play(*t.show())
    scene.wait(2)

class Main(Scene):
    def construct(self):
        video_name = r"""
        why probabilistic programming?
        """
        play_intro_scene(self, video_name)
        play_demo_scene(self)
        self.wait(1)
        self.clear()
        self.wait(2)
