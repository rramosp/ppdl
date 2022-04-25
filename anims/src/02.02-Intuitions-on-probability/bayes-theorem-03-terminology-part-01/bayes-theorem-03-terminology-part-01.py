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

        video_name = r"bayes-theorem-03-terminology-part-01"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-03-terminology-part-01-ES")
        
        self.add_sound(sfile)


        bayes_p_disease_to_positive = MathTex(
            "P","(","disease","|","positive", ")" , "=", 
            "{P(","positive", "|", "disease", ")", "\cdot", "P(disease)",
            "\\over", "P(", "positive", ")}" , color= BLACK
        ).scale(1).shift(UP)
        bayes_p_disease_to_positive.set_color_by_tex("positive",RED_E)

        timer.wait_until(29)

        self.play(Write(bayes_p_disease_to_positive), run_time=3)

        timer.wait_until(35)

        self.play(Indicate(bayes_p_disease_to_positive[2], color=BLUE_E, run_time=4,scale_factor=1.05),
                 Indicate(bayes_p_disease_to_positive[4], color=BLUE_E,run_time=4,scale_factor=1.05)
        )

        timer.wait_until(40)

        self.play(Indicate(bayes_p_disease_to_positive[:6],color= RED_E, run_time=4,scale_factor=1.05),
                  Indicate(bayes_p_disease_to_positive[7:12],color= RED_E, run_time=4,scale_factor=1.05),
                  Indicate(bayes_p_disease_to_positive[-5],color= RED_E, run_time=4,scale_factor=1.05),
                  Indicate(bayes_p_disease_to_positive[-3:],color= RED_E, run_time=4,scale_factor=1.05)
        )

        timer.wait_until(46)

        posterior_brace = Brace(bayes_p_disease_to_positive[:6],direction=UP,color=BLACK)

        posterior_tex = MathTex("Posterior", color=BLACK).scale(0.8).next_to(posterior_brace,UP)

        self.play(FadeIn(posterior_brace))

        timer.wait_until(58)

        self.play(Write(posterior_tex), run_time=2)

        timer.wait_until("1min 7sec")

        self.play(Indicate(posterior_tex, color=BLUE_E, run_time=3))

        timer.wait_until("1min 12sec")

        updating_animation(bayes_p_disease_to_positive[:6], self)

        timer.wait_until("1min 17sec")

        prior_brace = Brace(bayes_p_disease_to_positive[-5], color=BLACK, direction=UP)
        prior_tex = MathTex("Prior", color=BLACK).scale(0.8).next_to(prior_brace,UP)

        self.play(FadeIn(prior_brace))

        timer.wait_until("1min 20sec")

        self.play(Write(prior_tex, run_time=2))

        timer.wait_until("1min 25sec")

        self.play(Indicate(bayes_p_disease_to_positive[-5], color=BLUE_E), run_time=10)

        timer.wait_until("1min 37sec")

        percent_pop_disease_30_tex = MathTex("30\%", color=BLACK).scale(0.7).next_to(prior_tex,RIGHT).shift(RIGHT*0.5)
        percent_pop_disease_1_tex = MathTex("1\%", color=BLACK).scale(0.7).next_to(percent_pop_disease_30_tex,RIGHT).shift(RIGHT*0.5)
        arrow_prior_30 = Arrow(start=prior_tex, end=percent_pop_disease_30_tex.get_edge_center(LEFT),color=BLACK)
        arrow_30_1 = Arrow(start=percent_pop_disease_30_tex.get_edge_center(RIGHT), end=percent_pop_disease_1_tex.get_edge_center(LEFT),color=BLACK)


        self.play(Write(percent_pop_disease_30_tex))
        self.play(Write(arrow_prior_30))

        timer.wait_until("1min 46sec")

        self.play(Write(percent_pop_disease_1_tex))
        self.play(Write(arrow_30_1))

        timer.wait_until("1min 56sec")

        likelihood_brace = Brace(bayes_p_disease_to_positive[7:12],color=BLACK,direction=UP)
        likelihood_tex = MathTex("Likelihood", color=BLACK).scale(0.7).next_to(likelihood_brace,UP)

        self.play(Write(likelihood_brace))

        timer.wait_until("2min")

        self.play(Write(likelihood_tex))

        timer.wait_until("2min 20sec")

        self.play(Indicate(bayes_p_disease_to_positive[7:12], color=BLUE_E, scale_factor=1.1 ), run_time=5)

        timer.wait_until("2min 36sec")

        disease_likelihood_underline = Underline(bayes_p_disease_to_positive[10], color=RED_E)

        self.play(Write(disease_likelihood_underline),Indicate(bayes_p_disease_to_positive[10],color=RED_E, scale_factor=1.1  ,run_time=2))

        timer.wait_until("3min 26 sec")

        self.play(Indicate(bayes_p_disease_to_positive[8],color=BLUE_E,scale_factor=1.1,run_time=5))

        timer.wait_until("3min 44sec")

        vgroup_bayes_equation = VGroup(bayes_p_disease_to_positive,disease_likelihood_underline,
                                likelihood_brace,likelihood_tex,prior_brace,prior_tex,
                                arrow_30_1,arrow_prior_30,percent_pop_disease_1_tex,
                                percent_pop_disease_30_tex,posterior_brace,posterior_tex
        )

        question_tex = Tex("If", " I had the disease", ", what is the probability of seeing what I saw?",color=BLACK)
        question_tex.set_color_by_tex("disease", RED_E)


        self.play(vgroup_bayes_equation.animate.shift(UP).scale(0.8))

        self.play(FadeIn(question_tex,run_time=3))

        updating_animation(question_tex,self)

        timer.wait_until("3min 54sec")

        updating_animation(bayes_p_disease_to_positive[8],self)


        timer.wait_until("4min 35sec")

        self.play(FadeOut(disease_likelihood_underline))
        self.play(vgroup_bayes_equation.animate.shift(LEFT*2.6))


        p_pos_not_disease = MathTex(
            "P(", "positive", "|" ,"\lnot disease",")", "=", "0.05",color=BLACK
        ).scale(0.8).next_to(bayes_p_disease_to_positive[-5],RIGHT).shift(RIGHT)
        p_pos_not_disease.set_color_by_tex("positive", RED_E)

        
        self.play(Write(p_pos_not_disease[0:-2], run_time=5))


        timer.wait_until("4min 44sec")

        self.play(Write(p_pos_not_disease[-2:]))

        timer.wait_until("5min 6sec")

        self.play(Circumscribe(bayes_p_disease_to_positive[10],color=BLUE_B,time_width=3,fade_out=True),
                  Circumscribe(p_pos_not_disease[3],color=BLUE_B,time_width=3)
        )
        self.play(Circumscribe(bayes_p_disease_to_positive[10],color=BLUE_B,time_width=3),
                  Circumscribe(p_pos_not_disease[3],color=BLUE_B,time_width=3)
        )


        timer.wait_until("5min 28sec")

        norm_factor_brace = Brace(bayes_p_disease_to_positive[-3:],direction=DOWN, color=BLACK )
        norm_factor_tex = MathTex("Normalization \hspace{0.2cm} Factor", color=BLACK).scale(0.8).scale(0.8).next_to(norm_factor_brace,DOWN)
        

        self.play(FadeIn(norm_factor_brace))

        timer.wait_until("5min 31sec")

        self.play(Write(norm_factor_tex))

        timer.wait_until("5min 36sec")

        self.play(Indicate(bayes_p_disease_to_positive[-3:], color= BLUE_E, scale_factor=1.1),run_time=4)

        timer.wait_until("5min 42sec")

        p_disease_to_pos_fracc = MathTex(
            "P(disease|", "positive",") = ", "{P(", "positive", "|disease)", "\\cdot" , "P(disease)",
            "\\over",
            "P(" , "positive", "|disease)", "\\cdot", "P(disease) " , " + ", "P(", "positive", "|" ,"\lnot" ,"disease)", "\\cdot" , "P(", "\lnot" ,"disease)}"
            , color= BLACK
        ).scale(0.8).next_to(question_tex,DOWN,buff=1)
        p_disease_to_pos_fracc.set_color_by_tex("positive", RED_E)



        self.play(FadeIn(p_disease_to_pos_fracc))

        timer.wait_until("5min 45sec")

        correct_case_disease_underline = Underline(p_disease_to_pos_fracc[9:14],color=RED_E)
        incorrect_case_disease_underline = Underline(p_disease_to_pos_fracc[-9:], color=GREEN_E)

        self.play(Write(correct_case_disease_underline), Write(incorrect_case_disease_underline))

        timer.wait_until("6min")

        denominator_brace = Brace(p_disease_to_pos_fracc[9:], color=BLACK,buff=0.1)

        generalization_p_pos = MathTex(
            "\sum_{i=1}^{n}P(A|B_{i})\cdot P(B_{i})", color=BLACK
        ).scale(0.8).next_to(denominator_brace,DOWN,buff=0.2)

        self.play(Write(denominator_brace))

        self.play(Write(generalization_p_pos),run_time=6)

        timer.wait_until("6min 7sec")

        self.play(Circumscribe(p_disease_to_pos_fracc[1],color=BLUE_B,time_width=3,fade_out=True),
                Circumscribe(p_disease_to_pos_fracc[1],color=BLUE_B,time_width=3,fade_out=True),
                Circumscribe(p_disease_to_pos_fracc[1],color=BLUE_B,time_width=3)
        )

        timer.wait_until("6min 17sec")

        self.play(Circumscribe(generalization_p_pos,color=BLUE_B,time_width=3,fade_out=True),
                  Circumscribe(generalization_p_pos,color=BLUE_B,time_width=3)
        )

        timer.wait_until("6min 28sec")

        updating_animation(p_disease_to_pos_fracc[3:8],self)

        timer.wait_until("6min 33sec")

        updating_animation(p_disease_to_pos_fracc[9:14],self)

        timer.wait_until("7min 6sec")

        updating_animation(p_disease_to_pos_fracc[9:],self)

        timer.wait_until("7min 11sec")

        updating_animation(p_disease_to_pos_fracc,self)




        timer.wait_until("7min 15sec")

         ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)