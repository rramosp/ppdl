import logging
import os, sys
from unicodedata import decimal

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
        
        video_name = r"bayes theorem example part 01"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-02-example-part1")
        self.add_sound(sfile)

        population_tex = MathTex(
            "POPULATION" , color= BLACK
        )

        timer.wait_until(22)
        
        self.play(Write(population_tex, run_time=2))

        timer.wait_until(27)

        with_medical_condition_circle = Circle(0.5, color = RED_E, fill_opacity = 0.6).shift(LEFT*1.2)
        without_medical_condition_circle = Circle(0.5,color= GREEN_E, fill_opacity = 0.6).next_to(with_medical_condition_circle,RIGHT,buff=1)

        medical_condition_tex = MathTex(
            "medical condition" , color= BLACK
        ).next_to(with_medical_condition_circle,DOWN).scale(0.5)

        no_medical_condition_tex = MathTex(
            "non medical condition" , color= BLACK
        ).next_to(without_medical_condition_circle,DOWN).scale(0.5)

        with_medical_condition_vgroup = VGroup(with_medical_condition_circle,medical_condition_tex)
        without_medical_condition_vgroup = VGroup(without_medical_condition_circle, no_medical_condition_tex)
        
        wrapper_circles_with_label_vgroup = VGroup(with_medical_condition_vgroup,without_medical_condition_vgroup)

        self.play(population_tex.animate.shift(2*UP).scale(0.7))
        self.play(FadeIn(with_medical_condition_circle), FadeIn(without_medical_condition_circle))

        timer.wait_until(41)

        self.play(Write(medical_condition_tex), Write(no_medical_condition_tex))

        timer.wait_until(58)

        wrapper_population_with_definitions_vgroup = VGroup(wrapper_circles_with_label_vgroup, population_tex)
        wrapper_circles_with_label_vgroup.shift(UP*1.2)
        surrounder_wrapper_popul_defs = SurroundingRectangle(wrapper_population_with_definitions_vgroup,color=BLACK,stroke_width=0.8)
        complete_pop_def_vgroup = VGroup(wrapper_population_with_definitions_vgroup, surrounder_wrapper_popul_defs)
        
        
        self.play(complete_pop_def_vgroup.animate.to_edge(UP,buff=0.1).scale(0.7))

        p_disease = MathTex(
            "P(disease)", "=", "0.3", color=BLACK
        )

        timer.wait_until("1min 3sec")

        self.play(Write(p_disease,run_time=5))

        timer.wait_until("1min 24sec")

        p_positive_to_disease = MathTex(
            "P", "(" ,"positive", "|", "disease", ")", "=", "0.85", color= BLACK
        ).next_to(p_disease,DOWN)
        p_positive_to_disease.set_color_by_tex("positive",RED_E)

        self.play(FadeIn(p_positive_to_disease[0]), FadeIn(p_positive_to_disease[1]),
                FadeIn(p_positive_to_disease[3]),
                FadeIn(p_positive_to_disease[5])
        )

        timer.wait_until("1min 31sec")

        self.play(Write(p_positive_to_disease[4]))

        timer.wait_until("1min 36sec")

        self.play(Write(p_positive_to_disease[2]))
        
        timer.wait_until("1min 39sec")

        self.play(Write(p_positive_to_disease[-1]), Write(p_positive_to_disease[-2]))

        timer.wait_until("1min 57sec")

        self.play(Indicate(with_medical_condition_vgroup, color = RED_E,run_time=2))

        timer.wait_until("2min 0sec")

        updating_animation(p_positive_to_disease,self)

        timer.wait_until("2min 12sec")

        p_disease_to_positive = MathTex(
            "P", "(", "disease", "|", "positive",")", color= BLACK
        ).next_to(p_positive_to_disease,DOWN)

        p_disease_to_positive.set_color_by_tex("positive", RED_E)

        self.play(Write(p_disease_to_positive[0]), Write(p_disease_to_positive[1]),
                    Write(p_disease_to_positive[3]), Write(p_disease_to_positive[5]))


        timer.wait_until("2min 16sec")

        self.play(Write(p_disease_to_positive[4],run_time=2))
        self.play(Indicate(p_disease_to_positive[4],color=RED,run_time=4))


        timer.wait_until("2min 29sec")

        self.play(Write(p_disease_to_positive[2]))


        timer.wait_until("2min 42sec")

        equations_part_01 = VGroup(p_disease,p_disease_to_positive,p_positive_to_disease)

        self.play(equations_part_01.animate.to_edge(LEFT,SMALL_BUFF).shift(UP*2).scale(0.6))

        timer.wait_until("2min 45sec")

        bayes_p_disease_to_positive = MathTex(
            "P","(","disease","|","positive", ")" , "=", 
            "{P(","positive", "|", "disease", ")", "\cdot", "P(disease)",
            "\\over", "P(", "positive", ")}" , color= BLACK
        ).scale(0.7).shift(UP)
        bayes_p_disease_to_positive.set_color_by_tex("positive",RED_E)

        self.play(Write(VGroup(*bayes_p_disease_to_positive[0:7]),run_time=5))

        timer.wait_until("7min 55sec")

        

        
