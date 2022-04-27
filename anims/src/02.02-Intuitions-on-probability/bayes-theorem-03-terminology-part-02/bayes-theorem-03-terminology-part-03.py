from __future__ import division
from gzip import WRITE
import logging
import os, sys
from unicodedata import decimal
from unittest import result

from numpy import vdot
from scipy.fftpack import shift

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *

sys.path.insert(0, ".")

config.max_files_cached = 1000



class Main(Scene):
    def construct(self):

        video_name = r"bayes-theorem-03-terminology-part-02"
        #play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-03-terminology-part-01-ES")
        
        self.add_sound(sfile)


        bayes_p_disease_to_positive = MathTex(
            "P","(","disease","|","positive", ")" , "=", 
            "{P(","positive", "|", "disease", ")", "\cdot", "P(disease)",
            "\\over", "P(", "positive", ")}" , color= BLACK
        ).scale(1).shift(UP)
        bayes_p_disease_to_positive.set_color_by_tex("positive",RED_E)

        posterior_brace = Brace(bayes_p_disease_to_positive[:6],direction=UP,color=BLACK)

        posterior_tex = MathTex("Posterior", color=BLACK).scale(0.8).next_to(posterior_brace,UP)
        prior_brace = Brace(bayes_p_disease_to_positive[-5], color=BLACK, direction=UP)
        prior_tex = MathTex("Prior", color=BLACK).scale(0.8).next_to(prior_brace,UP)
        likelihood_brace = Brace(bayes_p_disease_to_positive[7:12],color=BLACK,direction=UP)
        likelihood_tex = MathTex("Likelihood", color=BLACK).scale(0.7).next_to(likelihood_brace,UP)
        norm_factor_brace = Brace(bayes_p_disease_to_positive[-3:],direction=DOWN, color=BLACK )
        norm_factor_tex = MathTex("Normalization \hspace{0.2cm} Factor", color=BLACK).scale(0.8).scale(0.8).next_to(norm_factor_brace,DOWN)
        

        self.play(Write(bayes_p_disease_to_positive))
        self.play(FadeIn(posterior_brace))
        self.play(Write(posterior_tex))
        self.play(FadeIn(prior_brace))
        self.play(Write(prior_tex))
        self.play(Write(likelihood_brace))
        self.play(Write(likelihood_tex))
        self.play(FadeIn(norm_factor_brace))
        self.play(Write(norm_factor_tex))
        
        timer.wait_until(10)

        


        timer.wait_until("10min 12sec")
        
        ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)