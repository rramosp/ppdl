import logging
import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *







class Main(Scene):
    def construct(self):
        video_name = r"Bayes theorem intuition"
        play_intro_scene(self,video_name)
        timer = SceneTimer(self,debug_wait=False).reset()
        sfile = find_soundfile("2022-01-12 15-40-29-bayes-theorem")

        self.add_sound(sfile)
        
