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

        video_name = r"bayes theorem example part 03"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-02-example-part-03-ES")
        
        self.add_sound(sfile)

        p_disease_to_pos_fracc = MathTex(
            "P(", "disease", "|", "positive",") = ", 
            "{P(", "positive", "|", "disease", ")", "\\cdot" , 
            "P(","disease",")",
            "\\over",
            "P(" , "positive", "|","disease",")", "\\cdot", 
            "P(","disease",") " , " + ", 
            "P(", "positive", "|" ,"\lnot disease",")", "\\cdot" , 
            "P(", "\lnot disease",")}"
            , color= BLACK
        ).shift(UP*0.5).scale(0.7)
        p_disease_to_pos_fracc.set_color_by_tex("disease", RED_E)
        p_disease_to_pos_fracc.set_color_by_tex("\lnot disease", GREEN_E)

        p_disease = MathTex(
            "P(", "disease",") = 0.01", color=BLACK
        ).next_to(p_disease_to_pos_fracc[0:5],DOWN).scale(0.7).shift(DOWN*2)
        p_disease.set_color_by_tex("disease", RED_E)


        not_sick_rectangle = Rectangle(width=2.8, height=3,color=GREEN_E, fill_opacity=0.1).shift(RIGHT*1).shift(UP*0.4).scale(0.65)
        sick_rectangle = Rectangle(width=1.3, height=3, color=RED_E, fill_opacity=0.1).scale(0.65).next_to(not_sick_rectangle,LEFT,buff=0)
        test_population_circle = Circle(color=BLACK).scale(0.7).move_to(sick_rectangle.get_edge_center(RIGHT)).shift(LEFT*0.3).scale(0.65)
        test_to_sick_intersection = Intersection(sick_rectangle,test_population_circle,color=ORANGE,fill_opacity=0.7)
        test_to_not_sick_intersection = Intersection(not_sick_rectangle,test_population_circle,color=PURPLE_A,fill_opacity=0.7)
        sick_to_test_difference = Difference(sick_rectangle,test_population_circle, color=RED_E,fill_opacity=0.2)
        not_sick_to_test_difference = Difference(not_sick_rectangle,test_population_circle,color=GREEN_E,fill_opacity=0.2)

        self.play(FadeIn(p_disease_to_pos_fracc,run_time=0.2))

        self.play(p_disease_to_pos_fracc.animate.shift(UP*0.6),run_time=0.2)

        self.play(Write(p_disease,run_time=0.2))

        p_pos_dis_9_12_underline = Underline(p_disease_to_pos_fracc[15:20],color=RED_E)

        tex_underline_1 = MathTex("0.85",color=BLACK).scale(0.6).next_to(p_pos_dis_9_12_underline,DOWN,buff=SMALL_BUFF)

        self.play(Write(p_pos_dis_9_12_underline), Write(tex_underline_1), run_time=0.2)

        p_pos_dis_13_underline = Underline(p_disease_to_pos_fracc[21:24],color=RED_E)

        tex_underline_2 = MathTex("0.01",color=BLACK).scale(0.6).next_to(p_pos_dis_13_underline,DOWN,buff=SMALL_BUFF)

        self.play(Write(p_pos_dis_13_underline),Write(tex_underline_2), run_time=0.2)

        p_pos_dis_m9_m4_underline = Underline(p_disease_to_pos_fracc[25:-4],color=RED_E)

        tex_underline_3 = MathTex("0.05",color=BLACK).scale(0.6).next_to(p_pos_dis_m9_m4_underline,DOWN,buff=SMALL_BUFF)
        tex_underline_3.set_color_by_tex("positive",RED_E)

        self.play(Write(p_pos_dis_m9_m4_underline), Write(tex_underline_3))

        p_pos_dis_m1_underline = Underline(p_disease_to_pos_fracc[-3:],color=RED_E)

        tex_underline_4 = MathTex("0.99",color=BLACK).scale(0.6).next_to(p_pos_dis_m1_underline,DOWN,buff=SMALL_BUFF)
        tex_underline_4.set_color_by_tex("positive",RED_E)

        self.play(Write(p_pos_dis_m1_underline),Write(tex_underline_4))

        tex_underline_5 = MathTex("0.85",color=BLACK).scale(0.6).next_to(p_disease_to_pos_fracc[5:9],UP,buff=SMALL_BUFF+0.1)
        tex_underline_6 = MathTex("0.01",color=BLACK).scale(0.6).next_to(p_disease_to_pos_fracc[11:14],UP,buff=SMALL_BUFF+0.1)

        self.play(Write(tex_underline_5),Write(tex_underline_6), run_time=0.2)

        p_disease_to_pos_fracc_upper_copy = p_disease_to_pos_fracc[5:10].copy()
        p_disease_to_pos_fracc_lower_copy = p_disease_to_pos_fracc[15:].copy()

        result_disease_to_positive = MathTex(
            "P(disease|", "positive",") = ", "{0.0085", "\\over", "0.058}", "=", "0.147"
            , color= BLACK
        ).scale(0.8).next_to(p_disease_to_pos_fracc,DOWN*4)
        result_disease_to_positive.set_color_by_tex("positive", RED_E)

        self.play(Write(result_disease_to_positive[:3]), Write(result_disease_to_positive[4]))
        self.play(ReplacementTransform(p_disease_to_pos_fracc_upper_copy,result_disease_to_positive[-5]),
                  ReplacementTransform(p_disease_to_pos_fracc_lower_copy,result_disease_to_positive[-3])    
        )        

        tex_p_pos_final = MathTex(
            "P(", "positive", ") = ", "0.058",color=BLACK
        ).next_to(p_disease,DOWN).scale(0.7)
        tex_p_pos_final.set_color_by_tex("positive", RED_E)

        self.play(Write(tex_p_pos_final), run_time=0.2)

        tex_p_pos_disease_final = MathTex(
            "P(disease|", "positive", ")", " = ", "0.147",color=BLACK
        ).next_to(tex_p_pos_final,DOWN).scale(0.7)
        tex_p_pos_disease_final.set_color_by_tex("positive",color=RED_E)

        self.play(Write(tex_p_pos_disease_final[:-2]),run_time=0.2)

        self.play(Write(tex_p_pos_disease_final[-2:]), Write(result_disease_to_positive[-2:]), run_time=0.2)



        timer.wait_until(11)

        starting_mobjects_vgroup = Group(*self.mobjects)

        self.play(starting_mobjects_vgroup.animate.shift(UP*2))
        self.play(result_disease_to_positive.animate.shift(LEFT*4))

        timer.wait_until(15)

        self.play(Write(sick_rectangle),run_time=3)

        timer.wait_until(21)

        self.play(Write(not_sick_rectangle,run_time=3))

        timer.wait_until(27)

        self.play(Write(test_population_circle), run_time=3)

        timer.wait_until(32)

        self.play(Write(test_to_not_sick_intersection),run_time=2)

        timer.wait_until(35)

        not_sick_rectangle_brace = Brace(test_to_not_sick_intersection,direction=RIGHT,buff=0,color=BLACK)
        not_sick_brace_label = MathTex("0.05", color =BLACK).scale(0.5).next_to(not_sick_rectangle_brace,RIGHT,buff=0.1)

        self.play(FadeIn(not_sick_rectangle_brace),run_time=2)
        self.play(FadeIn(not_sick_brace_label))

        timer.wait_until(41)

        self.play(Write(test_to_sick_intersection), run_time=2)

        timer.wait_until(44)

        #sick_rectangle_brace = Brace(sick_rectangle,direction=UP,buff=0,color=BLACK)
        sick_brace_label = MathTex("0.85", color =BLACK).scale(0.5).move_to(test_to_sick_intersection.get_center())

        #self.play(FadeIn(sick_rectangle_brace), run_time=2)
        self.play(FadeIn(sick_brace_label))

        timer.wait_until(51)

        self.play(Indicate(sick_brace_label,color=RED_E),Indicate(not_sick_brace_label,color=GREEN_E), run_time=5)

        timer.wait_until(56)

        self.play(Indicate(p_disease,color=RED_E,run_time=4))

        timer.wait_until("1min 20sec")

        self.play(Indicate(test_population_circle,run_time=5))

        timer.wait_until("1min 30sec")

        ## start second example of benn diagrams mobjects

        second_sick_rectangle = Rectangle(width=0.555, height=3, color=RED_E, fill_opacity=0.1
                         ).scale(0.65
                        ).next_to(not_sick_rectangle,RIGHT,buff=0).shift(RIGHT)

        

        second_not_sick_rectangle = Rectangle(width=3.545, height=3,color=GREEN_E, fill_opacity=0.1
                        ).scale(0.65).next_to(second_sick_rectangle,RIGHT,buff=0)

        

        second_test_population_circle = Circle(color=BLACK).scale(0.7).move_to(second_sick_rectangle.get_edge_center(RIGHT)).shift(RIGHT*0.18).scale(0.65)
        second_test_to_sick_intersection = Intersection(second_sick_rectangle,second_test_population_circle,color=ORANGE,fill_opacity=0.7)
        second_test_to_not_sick_intersection = Intersection(second_not_sick_rectangle,second_test_population_circle,color=PURPLE_A,fill_opacity=0.7)
        second_sick_to_test_difference = Difference(second_sick_rectangle,second_test_population_circle, color=RED_E,fill_opacity=0.2)
        second_not_sick_to_test_difference = Difference(second_not_sick_rectangle,second_test_population_circle,color=GREEN_E,fill_opacity=0.2)

        second_sick_rectangle_brace = Brace(second_sick_rectangle,direction=UP,color=BLACK,buff=0)
        second_sick_rectangle_brace_tex = MathTex("0.01", color=BLACK).scale(0.5).next_to(second_sick_rectangle_brace,UP,buff=0.1)

        second_not_sick_rectangle_brace = Brace(second_not_sick_rectangle,direction=UP,color=BLACK,buff=0)
        second_not_sick_rectangle_brace_tex = MathTex("0.99", color=BLACK).scale(0.5).next_to(second_not_sick_rectangle_brace,UP,buff=0.1)

        arrow_1 = Arrow(start=not_sick_rectangle.get_edge_center(RIGHT),end = second_sick_rectangle.get_edge_center(LEFT),color=BLACK )
        
        self.play(Write(second_sick_rectangle,run_time=3))
        self.play(Write(arrow_1))
        self.play(Write(second_sick_rectangle_brace), Write(second_sick_rectangle_brace_tex))


        timer.wait_until("1min 38sec")

        self.play(Write(second_not_sick_rectangle,run_time=5))
        self.play(FadeIn(second_not_sick_rectangle_brace), FadeIn(second_not_sick_rectangle_brace_tex))

        timer.wait_until("1min 46sec")

        self.play(FadeIn(second_test_population_circle))

        timer.wait_until("1min 50sec")

        self.play(Write(second_test_to_not_sick_intersection))

        timer.wait_until("1min 55sec")

        tex_inside_second_intersection_not_sick = MathTex("0.05", color=BLACK).scale(0.5).move_to(second_test_to_not_sick_intersection.get_center())

        self.play(Write(tex_inside_second_intersection_not_sick))
        self.play(Indicate(second_test_to_not_sick_intersection,color=PURPLE_A),run_time=4)

        timer.wait_until("2min")

        self.play(Write(second_test_to_sick_intersection))

        timer.wait_until("2min 6sec")

        #brace_second_test_to_sick_intersection = Brace(second_test_to_sick_intersection,color=BLACK,direction=DOWN,buff=0)
        second_test_to_sick_intersection_brace_tex = MathTex("0.85", color=BLACK).scale(0.4).move_to(second_test_to_sick_intersection.get_center())
        #self.play(Write(brace_second_test_to_sick_intersection))
        self.play(Write(second_test_to_sick_intersection_brace_tex))

        self.play(Indicate(second_test_to_sick_intersection,color=ORANGE,run_time=8))

        timer.wait_until("2min 20sec")

        self.play(Indicate(sick_rectangle,color=RED_E), Indicate(second_sick_rectangle,color=RED_E))
        self.play(Indicate(not_sick_rectangle,color=GREEN_E), Indicate(second_not_sick_rectangle,color=GREEN_E))


        timer.wait_until("2min 26sec")

        self.play(Indicate(second_test_to_not_sick_intersection,color=PURPLE_A), run_time=4)

        timer.wait_until("2min 31sec")

        self.play(Indicate(second_test_to_sick_intersection,color=ORANGE),run_time=6)

        timer.wait_until("2min 56sec")

        self.play(Indicate(test_to_sick_intersection,color=ORANGE),run_time=5)
        
        timer.wait_until("3min 3sec")

        self.play(Indicate(test_to_not_sick_intersection,color=PURPLE_A),run_time=6)

        timer.wait_until("3min 34sec")

        #arrow_left = Arrow(start=VGroup(sick_rectangle, not_sick_rectangle), end=)

        division_line = Line(start=ORIGIN, end=LEFT*2,color=BLACK).next_to(VGroup(sick_rectangle,not_sick_rectangle),DOWN).shift(DOWN*1.5)

        p_d_pos = MathTex("P(","disease","|", "positive", ") =", color=BLACK).scale(0.7).next_to(division_line,LEFT)
        p_d_pos.set_color_by_tex("positive",RED_E)

        copy_test_to_sick_intersection = test_to_sick_intersection.copy()
        copy_second_test_to_sick_intersection = second_test_to_sick_intersection.copy()
        copy_test_population_circle = VGroup(test_to_sick_intersection.copy(), test_to_not_sick_intersection.copy())
        copy_second_test_population_circle = VGroup(second_test_to_sick_intersection.copy(), second_test_to_not_sick_intersection.copy())


        self.play(Write(p_d_pos),run_time=4)

        timer.wait_until("3min 49sec")

        self.play(Write(division_line))
        self.play(copy_test_population_circle.animate.next_to(division_line,DOWN))

        timer.wait_until("3min 56sec")

        self.play(Indicate(p_d_pos[1],color=RED_E),run_time=3)

        timer.wait_until("4min")

        self.play(copy_test_to_sick_intersection.animate.next_to(division_line,UP))

        timer.wait_until("4min 3sec")

        arrow_2 = arrow_1.copy().shift(DOWN*2.5)

        division_line_2 = Line(start=ORIGIN, end=LEFT*2,color=BLACK
                            ).next_to(VGroup(second_sick_rectangle,second_not_sick_rectangle),DOWN
                            ).shift(DOWN*1.5)

        self.play(Write(division_line_2))
        self.play(Write(arrow_2))

        timer.wait_until("4min 20sec")

        self.play(copy_second_test_population_circle.animate.next_to(division_line_2,DOWN))
        
        timer.wait_until("4min 26sec")

        self.play(copy_second_test_to_sick_intersection.animate.next_to(division_line_2,UP))

        timer.wait_until("4min 42sec")

        left_division_vgroup = VGroup(division_line,copy_test_population_circle,copy_test_to_sick_intersection)
        right_division_vgroup = VGroup(division_line_2,copy_second_test_population_circle,copy_second_test_to_sick_intersection)
        
        surrounder_left_division = SurroundingRectangle(left_division_vgroup,color=BLUE_E)
        surrounder_right_division = SurroundingRectangle(right_division_vgroup,color=BLUE_E)

        self.play(Write(surrounder_left_division))
        self.play(Write(MathTex("0.879",color=BLACK).scale(0.7).next_to(surrounder_left_division,DOWN,buff=0.1)))

        timer.wait_until("4min 44sec")

        self.play(Write(surrounder_right_division))
        self.play(Write(MathTex("0.147",color=BLACK).scale(0.7).next_to(surrounder_right_division,DOWN,buff=0.1)))


        timer.wait_until("5min 13sec")


         ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)