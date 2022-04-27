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


def stickman_population(scene):

    sick_stickman_matrix = []
        
    rows = 4
    columns = 2

    for i in range(rows):
        row_list = []
        for j in range(columns):
            row_list.append(generate_stickman(size = 0.2, fill_opacity = 0.5,general_color = RED_E))
            if i == 0:
                if j == 0:
                    row_list[j].to_edge(UP,buff=MED_SMALL_BUFF).shift(LEFT*0.8).shift(DOWN*0.15)
                    scene.play(Write(row_list[j]),run_time=0.4)
                else:
                    row_list[j].next_to(row_list[j-1],RIGHT ,buff=0.2)
                    scene.play(Write(row_list[j]),run_time=0.4)         
            else:
                if j == 0:
                    row_list[j].next_to(sick_stickman_matrix[i-1][0],DOWN, buff = 0.15)
                    scene.play(Write(row_list[j]),run_time=0.4) 
                else:
                    row_list[j].next_to(row_list[j-1],RIGHT ,buff=0.2)
                    scene.play(Write(row_list[j],run_time=0.3))     

        sick_stickman_matrix.append(row_list)

    not_sick_stickman_matrix = []
    
    rows = 4
    columns = 4

    for i in range(rows):
        row_list = []
        for j in range(columns):
            row_list.append(generate_stickman(size = 0.2, fill_opacity = 0.5,general_color = GREEN_E))
            if i == 0:
                if j == 0:
                    row_list[j].next_to(sick_stickman_matrix[0][1],RIGHT,buff=0.3)
                    scene.play(Write(row_list[j]),run_time=0.3)
                else:
                    row_list[j].next_to(row_list[j-1],RIGHT ,buff=0.2)
                    scene.play(Write(row_list[j]),run_time=0.3)         
            else:
                if j == 0:
                    row_list[j].next_to(not_sick_stickman_matrix[i-1][0],DOWN, buff = 0.15)
                    scene.play(Write(row_list[j]),run_time=0.1) 
                else:
                    row_list[j].next_to(row_list[j-1],RIGHT ,buff=0.2)
                    scene.play(Write(row_list[j],run_time=0.1))     

        not_sick_stickman_matrix.append(row_list)
    return sick_stickman_matrix,not_sick_stickman_matrix

class Main(Scene):
    def construct(self):
        
        video_name = r"bayes theorem example part 02"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-02-example-part-02-ES")
        
        self.add_sound(sfile)     

        p_positive = MathTex(
            "P(","positive", ")", "=", "P(", "positive", "|", "disease", ")","\cdot",
            "P(", "disease", ")", "+", "P(", "positive", "|", "\lnot disease", ")","\cdot", "P(", "\lnot disease", ")"
            , color=BLACK
        ).scale(0.7).shift(DOWN*0.4)

        p_positive.set_color_by_tex("disease",RED_E)
        p_positive.set_color_by_tex("\lnot disease",GREEN_E)

        p_disease = MathTex(
            "P(", "disease", ")",  "=", "0.3"
            ,color=BLACK
        ).to_corner(UP+LEFT,buff=MED_SMALL_BUFF).shift(RIGHT*0.2).scale(0.7)
        p_disease.set_color_by_tex("disease",RED_E)
        p_disease.set_color_by_tex("disease",RED_E)

        p_not_disease = MathTex(
            "P(", "\lnot disease", ")", "=", "0.7" 
            , color = BLACK
        ).next_to(p_disease,DOWN).scale(0.7)
        p_not_disease.set_color_by_tex("\lnot disease",GREEN_E)
        p_not_disease.set_color_by_tex("\lnot disease",GREEN_E)

        p_positive_to_disease = MathTex(
            "P", "(" ,"positive", "|", "disease", ")", "=", "0.85", color= BLACK
        ).next_to(p_not_disease,DOWN).scale(0.6)
        p_positive_to_disease.set_color_by_tex("disease",RED_E)

        false_positive_tex = MathTex(
            "P(", "positive", "|", "\lnot disease) = " , "0.05", color=BLACK
        ).next_to(p_positive_to_disease,DOWN).scale(0.6)
        false_positive_tex.set_color_by_tex("\lnot disease",GREEN_E)

        bayes_theorem_disease = MathTex(
            "P(", "disease", "|","positive",")", " = ", "{P(", "positive", "|", "disease", ")", "\\cdot", "P(", "disease", ")",
             "\\over" ,
             "P(","positive",")}", color=BLACK
        ).to_edge(DOWN,buff=SMALL_BUFF).scale(0.6)

        bayes_theorem_disease.set_color_by_tex("disease",RED_E)

        ## HERE WE HAVE ALL THE SHAPES FOR THE VENN-LIKE DIAGRAMS

        not_sick_rectangle = Rectangle(width=2.8, height=3,color=GREEN_E, fill_opacity=0.1).to_corner(RIGHT+UP,buff=MED_SMALL_BUFF).shift(LEFT*4)
        sick_rectangle = Rectangle(width=1.3, height=3, color=RED_E, fill_opacity=0.1).next_to(not_sick_rectangle,LEFT,buff=0)
        test_population_circle = Circle(color=BLACK).scale(0.7).move_to(sick_rectangle.get_edge_center(RIGHT)).shift(LEFT*0.3)
        test_to_sick_intersection = Intersection(sick_rectangle,test_population_circle,color=ORANGE,fill_opacity=0.7)
        test_to_not_sick_intersection = Intersection(not_sick_rectangle,test_population_circle,color=PURPLE_A,fill_opacity=0.7)
        sick_to_test_difference = Difference(sick_rectangle,test_population_circle, color=RED_E,fill_opacity=0.2)
        not_sick_to_test_difference = Difference(not_sick_rectangle,test_population_circle,color=GREEN_E,fill_opacity=0.2)


        timer.wait_until(3)

        #self.play(FadeIn(bayes))
        sick_stickman_matrix,not_sick_stickman_matrix = stickman_population(self)

        timer.wait_until(11)

        self.play(FadeIn(p_positive))

        timer.wait_until(28)

        self.play(Write(p_disease),run_time=5)

        timer.wait_until(38)

        self.play(Write(p_not_disease), run_time=3)

        timer.wait_until(47)

        self.play(Write(p_positive_to_disease), run_time=8)

        timer.wait_until(56)

        self.play(Write(false_positive_tex),run_time=3)

        timer.wait_until("1min 5sec")

        ### start picking up stickmans
        stickman_test_list = [sick_stickman_matrix[0][0], sick_stickman_matrix[0][1],
                             sick_stickman_matrix[1][0], sick_stickman_matrix[1][1],
                             sick_stickman_matrix[2][0], sick_stickman_matrix[2][1],
                             sick_stickman_matrix[3][1], not_sick_stickman_matrix[3][0]
                            ]

        self.play(Indicate(Group(*stickman_test_list),scale_factor=1.1,run_time=9 ))
        
        timer.wait_until("1min 17sec")

        self.play(Indicate(Group(p_positive_to_disease, false_positive_tex), color=BLUE_E, run_time=3))

        timer.wait_until("1min 25sec")

        updating_animation(sick_stickman_matrix[3][0], self)
        
        timer.wait_until("1min 34sec")

        updating_animation(not_sick_stickman_matrix[3][0], self)

        timer.wait_until("1min 41sec")

        updating_animation(p_positive_to_disease[-1], self)

        timer.wait_until("2min")

        self.play(Write(sick_rectangle,run_time=4))
        self.play(Write(not_sick_rectangle))
        

        timer.wait_until("2min 8sec")

        for i in sick_stickman_matrix:
            self.play(FadeOut(*i),run_time=0.2)
        for i in not_sick_stickman_matrix:
            self.play(FadeOut(*i),run_time=0.1)

        timer.wait_until("2min 9sec")

        self.play(Indicate(sick_rectangle,color=RED_E, run_time=3))
        self.play(Indicate(not_sick_rectangle,color=GREEN_E, run_time=3))

        timer.wait_until("2min 19sec")

        self.play(Write(test_population_circle,run_time=3))

        timer.wait_until("2min 31sec")

        self.play(FadeIn(test_to_sick_intersection),run_time=2)
        self.play(Indicate(test_to_sick_intersection,color=ORANGE),run_time=2)

        timer.wait_until("2min 37sec")

        self.play(FadeIn(test_to_not_sick_intersection),run_time=2)
        self.play(Indicate(test_to_not_sick_intersection,color=PURPLE_A),run_time=3)

        timer.wait_until("2min 46sec")

        self.play(FadeIn(not_sick_to_test_difference,run_time=2))
        self.play(Indicate(not_sick_to_test_difference,color=GREEN_E,run_time=5))

        timer.wait_until("2min 53sec")

        self.play(FadeIn(sick_to_test_difference,run_time=2))
        self.play(Indicate(sick_to_test_difference,run_time=5))

        timer.wait_until("3min 5sec")

        self.play(Write(bayes_theorem_disease,run_time=14))

        timer.wait_until("3min 26sec")

        surrounder_1 = SurroundingRectangle(bayes_theorem_disease[6:11], buff= .06)

        self.play(Write(surrounder_1))

        #p_positive = MathTex(
        #    "P(","positive", ")", "=", "P(", "positive", "|disease)","\cdot",
        #    "P(disease)", "+", "P(", "positive", "|", "\lnot" ,"disease)","\cdot", "P(", "\lnot" ,"disease)"
        #    , color=BLACK
    
        timer.wait_until("3min 29sec")

        self.play(Indicate(test_to_sick_intersection,color=ORANGE),run_time=4)

        timer.wait_until("3min 39sec")

        division_line = Line(ORIGIN, LEFT*2).next_to(p_positive[4:9],DOWN,buff=MED_SMALL_BUFF).shift(DOWN*1)

        copy_sick_rectangle = sick_rectangle.copy()
        copy_test_to_sick_intersection = test_to_sick_intersection.copy()

        p_pos_to_disease_division = VGroup(division_line,copy_sick_rectangle,copy_test_to_sick_intersection)

        self.play(Write(division_line.scale(0.5)))

        timer.wait_until("3min 50sec")

        self.play(copy_sick_rectangle.animate.next_to(division_line,DOWN,buff=0).shift(UP*0.9).scale(0.3))

        timer.wait_until("4min 22sec")

        self.play(copy_test_to_sick_intersection.animate.next_to(division_line,UP,buff=0).shift(DOWN*0.2).scale(0.5))

        timer.wait_until("4min 27sec")

        updating_animation(bayes_theorem_disease[6:11],self)

        timer.wait_until("4min 38sec")

        surrounder_2 = SurroundingRectangle(bayes_theorem_disease[12:15], buff=.06)

        self.play(ReplacementTransform(surrounder_1,surrounder_2))

        timer.wait_until("4min 40sec")

        self.play(Indicate(sick_rectangle,color=RED_E), run_time = 2)

        timer.wait_until("4min 42sec")

        copy_2_sick_rectangle = copy_sick_rectangle.copy().next_to(p_positive[10:13],DOWN,buff=MED_SMALL_BUFF).shift(DOWN*0.3)

        self.play(Write(MathTex("\\cdot", color=BLACK).scale(2).next_to(division_line,RIGHT).shift(RIGHT*0.35)),
                 ReplacementTransform(copy_sick_rectangle.copy(), copy_2_sick_rectangle)
        )

        timer.wait_until("4min 44sec")

        self.play(FadeOut(surrounder_1,surrounder_2))


        timer.wait_until("4min 57sec")

        ppos_first_half_underline = Underline(p_positive[4:13], color=BLUE_E)
        ppos_second_half_underline = Underline(p_positive[14:], color=BLUE_E)

        self.play(Write(ppos_first_half_underline),run_time=1)
        self.play(Write(ppos_second_half_underline),run_time=2)
        

        timer.wait_until("5min 6sec")

        self.play(Indicate(p_positive[4:9],color=RED_E, scale_factor=1.05,run_time=2))
        self.play(Indicate(p_pos_to_disease_division,color=BLUE_E ,run_time=2))
        
        timer.wait_until("5min 10sec")

        self.play(Indicate(p_positive[14:-4],color=GREEN_E, scale_factor=1.05,run_time=4))

        timer.wait_until("5min 19sec")

        surrounder_p_pos_1 = SurroundingRectangle(p_positive[14:-4],buff=0.06)

        self.play(Write(surrounder_p_pos_1))
        #self.play(p_pos_to_disease_division.animate.shift(LEFT))

        division_line_2 = Line(ORIGIN, LEFT*2).scale(0.5).next_to(p_positive[14:-4],DOWN,buff=MED_SMALL_BUFF).shift(DOWN*1)
        not_sick_rectangle_copy = not_sick_rectangle.copy()
        test_to_not_sick_intersection_copy = test_to_not_sick_intersection.copy()
        second_division_vgroup = VGroup(division_line_2,not_sick_rectangle_copy,test_to_not_sick_intersection)

        self.play(Write(MathTex("+",color=BLACK).scale(1.5).next_to(division_line_2,LEFT).shift(LEFT*0.35))
        )

        self.play(Write(division_line_2))
        self.play(not_sick_rectangle_copy.animate.next_to(division_line_2,DOWN,buff=0).shift(UP).scale(0.3).scale(0.7))

        timer.wait_until("5min 26sec")

        self.play(FadeOut(surrounder_p_pos_1))

        self.play(Indicate(not_sick_rectangle,color=GREEN_E), run_time=2)

        timer.wait_until("5min 35sec")

        self.play(Indicate(test_to_not_sick_intersection,color=PURPLE_A),run_time=2)

        timer.wait_until("5min 38sec")

        self.play(test_to_not_sick_intersection_copy.animate.next_to(division_line_2,UP,buff=0).shift(DOWN*0.2).scale(0.5))

        not_sick_rectangle_copy_2 = not_sick_rectangle_copy.copy().next_to(p_positive[-3:],DOWN,buff=MED_SMALL_BUFF).shift(DOWN*0.65)

        self.play(Write(MathTex("\\cdot", color=BLACK).scale(2).next_to(division_line_2,RIGHT).shift(RIGHT*0.35)),
                 ReplacementTransform(not_sick_rectangle_copy.copy(), not_sick_rectangle_copy_2)
        )

        timer.wait_until("5min 44sec")

        self.play(Indicate(p_positive[4:13],scale_factor=1.11, run_time= 2, color=RED_E))

        timer.wait_until("5min 47sec")

        self.play(Indicate(p_positive[0:3],scale_factor=1.1 ,run_time=2, color=RED_E))

        timer.wait_until("5min 49sec")

        self.play(Indicate(test_population_circle,scale_factor=1.4,color=BLACK,run_time=4))

        timer.wait_until("5min 55sec")

        self.play(Indicate(test_to_sick_intersection,color=ORANGE),run_time=3)

        timer.wait_until("6min 2sec")

        copy_2_test_to_sick_intersection = test_to_sick_intersection.copy()
        copy_2_test_to_not_sick_intersection = test_to_not_sick_intersection.copy()

        self.play(copy_2_test_to_sick_intersection.animate.next_to(p_positive[0],DOWN,buff=MED_SMALL_BUFF).shift(DOWN*0.3))

        timer.wait_until("6min 6sec")

        self.play(copy_2_test_to_not_sick_intersection.animate.next_to(copy_2_test_to_sick_intersection,RIGHT,buff=0))
        self.play(Write(MathTex("=", color=BLACK).scale(1.4).next_to(copy_2_test_to_not_sick_intersection, RIGHT, buff=MED_SMALL_BUFF)))

        timer.wait_until("6min 9sec")

        cancel_line_1 = Line(start=LEFT, end=UP+RIGHT*1.3).move_to(not_sick_rectangle_copy.get_center_of_mass()).scale(0.5)
        cancel_line_2 = Line(start=LEFT, end=UP+RIGHT*1.3).move_to(not_sick_rectangle_copy_2.get_center()).scale(0.5)

        cancel_line_3 = Line(start=LEFT, end=UP+RIGHT*1.3).move_to(copy_sick_rectangle.get_center_of_mass()).scale(0.5)
        cancel_line_4 = Line(start=LEFT, end=UP+RIGHT*1.3).move_to(copy_2_sick_rectangle.get_center()).scale(0.5)

        self.play(FadeIn(cancel_line_1), FadeIn(cancel_line_2), FadeIn(cancel_line_3), FadeIn(cancel_line_4) )


        timer.wait_until("6min 28sec")

        self.play(FadeOut(*self.mobjects))

        p_disease_to_pos_fracc = MathTex(
            "P(", "disease", "|", "positive",") = ", 
            "{P(", "positive", "|", "disease", ")", "\\cdot" , 
            "P(", "disease", ")",
            "\\over",
            "P(" , "positive", "|", "disease", ")", "\\cdot", 
            "P(", "disease", ") " , " + ", "P(", "positive", "|" ,"\lnot disease", ")", "\\cdot" , 
            "P(", "\lnot disease", ")}"
            , color= BLACK
        ).shift(UP*0.5).scale(0.7)
        p_disease_to_pos_fracc.set_color_by_tex("disease", RED_E)
        p_disease_to_pos_fracc.set_color_by_tex("\lnot disease", GREEN_E)

        p_disease = MathTex(
            "P(", "disease", ") = 0.01", color=BLACK
        ).next_to(p_disease_to_pos_fracc[0:5],DOWN).scale(0.7).shift(DOWN*2)
        p_disease.set_color_by_tex("disease", RED_E)

        self.play(FadeIn(p_disease_to_pos_fracc))

        timer.wait_until("6min 46sec")

        self.play(p_disease_to_pos_fracc.animate.shift(UP*0.6))

        self.play(Write(p_disease,run_time=9))

        timer.wait_until("7min 19sec")

        self.play(Indicate(p_disease_to_pos_fracc[5:10], color= BLUE_E), 
                  Indicate(p_disease_to_pos_fracc[15:20],color=BLUE_E))

        timer.wait_until("7min 21sec")

        self.play(Indicate(p_disease_to_pos_fracc[-9:-4],color=BLUE_E))

        timer.wait_until("7min 33sec")
        
        self.play(Indicate(p_disease_to_pos_fracc[11:14],color=BLUE_E))

        timer.wait_until("7min 35sec")

        self.play(Indicate(p_disease_to_pos_fracc[21:24],color=BLUE_E))

        timer.wait_until("7min 37sec")

        self.play(Indicate(p_disease_to_pos_fracc[-3:],color=BLUE_E))

        timer.wait_until("7min 45sec")

        self.play(Indicate(p_disease_to_pos_fracc[15:],color=BLUE_E,scale_factor=1.05),run_time=10)

        timer.wait_until("7min 56sec")

        p_pos_dis_9_12_underline = Underline(p_disease_to_pos_fracc[15:20],color=RED_E)

        tex_underline_1 = MathTex("0.85",color=BLACK).scale(0.6).next_to(p_pos_dis_9_12_underline,DOWN,buff=SMALL_BUFF)

        self.play(Write(p_pos_dis_9_12_underline))
        self.play(Write(tex_underline_1,run_time=3))

        timer.wait_until("8min 2sec")
        print ("XX", p_disease_to_pos_fracc[21:24])
        p_pos_dis_13_underline = Underline(p_disease_to_pos_fracc[21:24],color=RED_E)

        tex_underline_2 = MathTex("0.01",color=BLACK).scale(0.6).next_to(p_pos_dis_13_underline,DOWN,buff=SMALL_BUFF)

        self.play(Write(p_pos_dis_13_underline))
        self.play(Write(tex_underline_2,run_time=2))

        timer.wait_until("8min 4sec")

        p_pos_dis_m9_m4_underline = Underline(p_disease_to_pos_fracc[-9:-4],color=RED_E)

        tex_underline_3 = MathTex("0.05",color=BLACK).scale(0.6).next_to(p_pos_dis_m9_m4_underline,DOWN,buff=SMALL_BUFF)
        tex_underline_3.set_color_by_tex("positive",RED_E)

        self.play(Write(p_pos_dis_m9_m4_underline))
        self.play(Write(tex_underline_3,run_time=2))

        timer.wait_until("8min 12sec") 

        p_pos_dis_m1_underline = Underline(p_disease_to_pos_fracc[-3:],color=RED_E)

        tex_underline_4 = MathTex("0.99",color=BLACK).scale(0.6).next_to(p_pos_dis_m1_underline,DOWN,buff=SMALL_BUFF)
        tex_underline_4.set_color_by_tex("positive",RED_E)

        self.play(Write(p_pos_dis_m1_underline))
        self.play(Write(tex_underline_4,run_time=2))

        timer.wait_until("8min 16sec")

        tex_underline_5 = MathTex("0.85",color=BLACK).scale(0.6).next_to(p_disease_to_pos_fracc[5:10],UP,buff=SMALL_BUFF+0.1)
        tex_underline_6 = MathTex("0.01",color=BLACK).scale(0.6).next_to(p_disease_to_pos_fracc[11:14],UP,buff=SMALL_BUFF+0.1)

        self.play(Write(tex_underline_5,run_time=2))
        self.play(Write(tex_underline_6,run_time=2))

        timer.wait_until("8min 22sec")

        p_disease_to_pos_fracc_upper_copy = p_disease_to_pos_fracc[5:14].copy()
        p_disease_to_pos_fracc_lower_copy = p_disease_to_pos_fracc[15:].copy()

        result_disease_to_positive = MathTex(
            "P(","disease", "|", "positive",") = ", "{0.0085", "\\over", "0.058}", "=", "0.147"
            , color= BLACK
        ).scale(0.8).next_to(p_disease_to_pos_fracc,DOWN*4)
        result_disease_to_positive.set_color_by_tex("disease", RED_E)

        self.play(Write(result_disease_to_positive[:5]), Write(result_disease_to_positive[6]))
        self.play(ReplacementTransform(p_disease_to_pos_fracc_upper_copy,result_disease_to_positive[-5]),
                  ReplacementTransform(p_disease_to_pos_fracc_lower_copy,result_disease_to_positive[-3])    
        )        

        timer.wait_until("8min 24sec")

        self.play(Circumscribe(result_disease_to_positive[-3],color=BLUE_B,time_width=3,fade_out=True),
                 Circumscribe(p_disease_to_pos_fracc[13:],color=BLUE_B,time_width=3,fade_out=True)
        )

        self.play(Circumscribe(result_disease_to_positive[-3],color=BLUE_B,time_width=3),
                 Circumscribe(p_disease_to_pos_fracc[13:],color=BLUE_B,time_width=3)
        )

        timer.wait_until("8min 27sec")

        tex_p_pos_final = MathTex(
            "P(", "positive", ") = ", "0.058",color=BLACK
        ).next_to(p_disease,DOWN).scale(0.7)

        self.play(Write(tex_p_pos_final,run_time=3))

        timer.wait_until("8min 33sec")

        tex_p_pos_disease_final = MathTex(
            "P(","disease","|", "positive", ")", " = ", "0.147",color=BLACK
        ).next_to(tex_p_pos_final,DOWN).scale(0.7)
        tex_p_pos_disease_final.set_color_by_tex("disease",color=RED_E)

        self.play(Write(tex_p_pos_disease_final[:-2],run_time=4))

        timer.wait_until("8min 44sec")

        self.play(Write(tex_p_pos_disease_final[-2:]), Write(result_disease_to_positive[-2:]))
        self.play(Indicate(tex_p_pos_disease_final[-1], color=BLUE_E),
                 Indicate(result_disease_to_positive[-1], color=BLUE_E),
                 run_time=3
        )

        timer.wait_until("8min 50sec")

        device_test = VGroup(p_disease_to_pos_fracc[5:10],p_disease_to_pos_fracc[15:20],p_disease_to_pos_fracc[-9:-4]  )

        self.play(Indicate(device_test,color=BLUE_E,scale_factor=1.08),run_time=5)

        timer.wait_until("9min 2sec")

        self.play(Indicate(tex_p_pos_disease_final[-1], color=RED_E),run_time=10)
        
        timer.wait_until("9min 23sec") 


        ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)

        