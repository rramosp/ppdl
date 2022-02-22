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

ES_text_dict = {}

def create_bayes_theorem_header(scene):
    ES_text_dict["bayes_theorem_header"] = "bayes theorem definition"
    text_bayes = Text(ES_text_dict["bayes_theorem_header"], color=BLUE_E ).to_edge(UP)
    scene.play(Write(text_bayes))
    return text_bayes

def create_bayes_theorem_definition(scene,header):
    
    text_latex_bayes_def_left = Tex(r'$$P(A|B)$$').scale(1)
    text_latex_bayes_def_right = Tex(r'$$ = \frac{P(B|A)P(A)}{P(B)}$$').scale(1)

    pairs = [("left",text_latex_bayes_def_left) , ("right", text_latex_bayes_def_right)]
    group_latex_bayes_def = VDict(pairs,show_keys=False)

    text_latex_bayes_def_left.next_to(text_latex_bayes_def_right,direction=LEFT)
    group_latex_bayes_def.next_to(header,direction=DOWN)

    scene.play(Write(group_latex_bayes_def),run_time=14,lag_ratio=0.5)

    return group_latex_bayes_def

def create_bayesian_inference_header(scene, split_line):
    ES_text_dict["bayesian_inference_1"] = "1. belief uncertainty"
    ES_text_dict["bayesian_inference_2"] = "2. belief updates"

    text_keypoint_one = Text(ES_text_dict["bayesian_inference_1"],color=BLUE_E,font_size=24).to_edge(LEFT)
    text_keypoint_two = Text(ES_text_dict["bayesian_inference_2"],color=BLUE_E,font_size=24).to_edge(RIGHT)

    pairs = [("left_keypoint", text_keypoint_one) , ("right_keypoint", text_keypoint_two)]
    group_keypoints_inference = VDict(pairs,show_keys=False)

    text_keypoint_one.align_to(split_line,UP)
    text_keypoint_two.align_to(split_line,UP)

    scene.play(Write(group_keypoints_inference))
    return group_keypoints_inference

def create_inference_bulletpoint_one(scene, inference_bulletpoints_header):
    ES_text_dict["bayesian_inference_belief"] = "new knowledge"
    ES_text_dict["bayesian_inference_uncertainty"] = "uncertainty"

    text_belief = Text(ES_text_dict["bayesian_inference_belief"],color=BLACK,font_size=20).to_edge(LEFT,buff=1.5)
    text_uncertainty = Text(ES_text_dict["bayesian_inference_uncertainty"],color=BLACK,font_size=20)

    text_belief.align_to(inference_bulletpoints_header["left_keypoint"],DOWN)
    text_belief.shift(DOWN*0.8)
    
    text_uncertainty.next_to(text_belief,RIGHT*4)

    double_arrow_belief_uncertainty = DoubleArrow(start=text_belief.get_right(),end=text_uncertainty.get_left(), color= BLUE_E)

    pairs = [("belief", text_belief) ,
             ("uncertainty", text_uncertainty),
             ("double_arrow" , double_arrow_belief_uncertainty) 
            ]

    header_keypoint_one = VDict(pairs, show_keys=False)

    scene.play(Write(text_belief))
    scene.play(Write(double_arrow_belief_uncertainty))
    #scene.play(Write(text_uncertainty))

    return header_keypoint_one

def create_inference_bulletpoint_one_example(scene, inference_bulletpoint_one):

    text_latex_rain = Tex("$$P(rain) = $$").scale(1)
    text_latex_rain.to_corner(DL,buff=2)


    decimal = DecimalNumber(0.5, color=BLACK)
    decimal.next_to(text_latex_rain, direction=RIGHT)
    

    scene.play(Write(text_latex_rain))
    scene.wait(2)
    scene.play(FadeIn(decimal))
    scene.wait(8)
    scene.play(Indicate(inference_bulletpoint_one["uncertainty"],color=RED_E,run_time=4))
    scene.wait(22)
    scene.play(FadeOut(decimal))
    decimal.set_value(1.0)
    scene.play(FadeIn(decimal))
    scene.wait(1)
    scene.play(Indicate(inference_bulletpoint_one["belief"],color=RED_E,run_time=8))
    scene.play(FadeOut(decimal))
    decimal.set_value(0.5)
    scene.play(FadeIn(decimal))
    return text_latex_rain,decimal

def create_inference_bulletpoint_two(scene, inference_bulletpoints_header):

    text_belief = Text(ES_text_dict["bayesian_inference_belief"],color=BLACK,font_size=22).to_edge(RIGHT,buff=2.7)

    text_belief.align_to(inference_bulletpoints_header["right_keypoint"],DOWN)
    text_belief.shift(DOWN*0.8)   

    pairs = [("belief", text_belief)
            ]

    header_keypoint_two = VDict(pairs, show_keys=False)

    scene.play(Write(text_belief,run_time=2))
    scene.play(Circumscribe(text_belief,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_belief,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_belief,color=BLUE_B,time_width=3))



    return header_keypoint_two


def create_inference_bulletpoint_two_example(scene, inference_bulletpoints_header):
    ES_text_dict["list_bulletpoint_two"] = "- observations\n\n- events\n\n- information"
    
    txt = Text(ES_text_dict["list_bulletpoint_two"],color=BLACK,font_size=16).to_edge(RIGHT, buff= 5).scale(1)
    txt.align_to(inference_bulletpoints_header["right_keypoint"],DOWN)
    txt.shift(DOWN*2)

    text_latex_rain = Tex("$$P(rain) = $$").scale(1).to_corner(DR,buff= 3)
    text_latex_rain.shift(DOWN*1)
    
    
    decimal_rain = DecimalNumber(0.5, color = BLACK)
    decimal_rain.next_to(text_latex_rain,direction=RIGHT)

    pairs = [ ("list_txt", txt), ("txt_latex", text_latex_rain), ("decimal", decimal_rain) ]

    bulletpoint_example_vdict = VDict(pairs,show_keys=False)

    scene.play(Write(txt.shift(DOWN*0.5),run_time=8.0))
    scene.wait(13)
    scene.play(Write(text_latex_rain))
    scene.play(Write(decimal_rain))
    scene.wait(26)
    scene.play(FadeOut(decimal_rain))
    decimal_rain.set_value(0.8)
    scene.play(FadeIn(decimal_rain))
    
    scene.wait(2)
    scene.play(Circumscribe(text_latex_rain,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_latex_rain,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_latex_rain,color=BLUE_B,time_width=3))
    scene.play(Indicate(txt), color=RED_E,run_time=14)
    scene.wait(1)

    return bulletpoint_example_vdict





class Main(Scene):
    def construct(self):

        video_name = r"bayes theorem intuition"
        play_intro_scene(self,video_name)
        timer = SceneTimer(self,debug_wait=False).reset()

        sfile = find_soundfile("01_bayes_theorem") 
        self.add_sound(sfile)
        
        self.next_section("1. Definition Bayes Theorem")
        timer.wait_until(3)
        bayes_theorem_intro = create_bayes_theorem_header(self)
        
        timer.wait_until(11)
        bayes_latex_theorem = create_bayes_theorem_definition(self, bayes_theorem_intro)
        timer.wait_until(35)

        self.play(Indicate(bayes_latex_theorem["left"]),color=RED_E,run_time=4)
        timer.wait_until(45)
        
        dot_bottom = Dot(color=BLUE_E)
        dot_bottom.to_edge(DOWN)

        split_line = Line(bayes_latex_theorem.get_bottom(), dot_bottom.get_center(),color=BLUE_E,stroke_width=2)
        self.play(Create(split_line))
        self.play(Create(dot_bottom))

        timer.wait_until("1min 2sec")
        self.play(bayes_latex_theorem.animate.scale(0.6))
        inference_bulletpoints_header = create_bayesian_inference_header(self,split_line)

        timer.wait_until("1min 15sec")
        self.play(Indicate(bayes_latex_theorem),color=RED_E,run_time=3)

        timer.wait_until("1min 33sec")
        self.play(Indicate(inference_bulletpoints_header["left_keypoint"]), color=RED_E,run_time=2)

        timer.wait_until("1min 36sec")
        inference_bulletpoint_one = create_inference_bulletpoint_one(self,inference_bulletpoints_header)      

        timer.wait_until("1min 55sec")
        inference_keypoint_one_example =  create_inference_bulletpoint_one_example(self,inference_bulletpoint_one)

        timer.wait_until("2min 45sec")
        self.play(Indicate(inference_bulletpoints_header["right_keypoint"]), color=RED_E,run_time=4)

        timer.wait_until("2min 51sec")
        inference_bulletpoint_two = create_inference_bulletpoint_two(self,inference_bulletpoints_header)

        timer.wait_until("2min 58sec")
        bulletpoint_two_example = create_inference_bulletpoint_two_example(self,inference_bulletpoints_header)


        self.play(*[FadeOut(mobject) for mobject in self.mobjects])

        timer.wait_until("4min 9sec")

        ### SECTION END ############

        self.next_section("2. Sun and Rain Example")
        
        sun_rain_example_title =  Text("sun and rain example", color=BLUE_E)
        self.play(FadeIn(sun_rain_example_title))

        timer.wait_until("4min 20sec")
        self.play(FadeOut(sun_rain_example_title,shift=DOWN))
        

        rain_circle = Circle(radius=3, color=BLUE_E,
                             fill_opacity=0.4, stroke_width=4).move_to(LEFT)
        sun_circle = Circle(radius=3, color=YELLOW_E,
                            fill_opacity=0.4, stroke_width=4).move_to(RIGHT*2.5)

        sun_label = MathTex("sun", color=BLACK).next_to(
            sun_circle.get_corner(UR), buff=0.1)
        rain_label = MathTex("rain", color=BLACK).next_to(
            rain_circle.get_corner(UL), buff=-1.5)

        pairs = [("Rain", rain_circle), ("Sun", sun_circle),
                 ("sun_label", sun_label), ("rain_label", rain_label)]

        circles_vdict = VDict(pairs, show_keys=False)

        p_rain_text = MathTex(
            "P(rain)=", "0.6", color=BLUE_E, stroke_width=2)

        p_sun_text = MathTex(
            "P(sun)= ", "0.4", color=YELLOW_E, stroke_width=2)

        p_rain_sun_text = MathTex(
            "P(rain + sun)=", "0.3", color=GREEN_E, stroke_width=0.8)

        p_sun_if_rain = MathTex(
            "P", "(", "sun", "|", "rain", ")", color=BLACK
        )

        p_sun_if_rain_longer = MathTex(
            "P(sun|rain)", "=", "{P(rain+sun)", "\\over", "P(rain)}", "=", color=BLACK)
        p_sun_if_rain_longer_numeric = MathTex(
            "\\frac{0.3}{0.6}", "=", "0.5", color=BLACK)

        p_rain_if_sun_longer = MathTex(
            "P(sun|rain)", "=", "{P(rain+sun)", "\\over", "P(sun)}", "=", color=BLACK)
        p_rain_if_sun_longer_numeric = MathTex(
            "\\frac{0.3}{0.4}", "=", "0.75", color=BLACK)

        p_rain_plus_sun_longer = MathTex(
            "P(rain+sun)", "=", "P(sun|rain)", "\cdot", "P(rain)", "=", "P(rain|sun)", "\cdot", "P(sun)", color=BLACK)

        bayes_with_sun_and_rain = MathTex(
            "P(sun|rain)", "=", "{P(rain|sun)", "\cdot", "P(sun)", "\\over", "P(rain)}", color=BLACK)

        bayes_definition_tex = MathTex("P","(","A","|","B",")","=","{P(B|A)","P(A)","\\over","P(B)} "," ; ",color=BLACK)

        rain_sun_to_definition = MathTex(r"If\ ",r"A = sun",r"\\",r"B = rainn",color=BLACK)

        expression_value_tex = Tex("value", color=BLACK)
        expression_meaning_tex = Tex("meaning", color=BLACK)

        timer.wait_until("4min 6sec")
        self.play(GrowFromCenter(circles_vdict, run_time=3))
        self.play(circles_vdict.animate.scale(0.4).to_edge(LEFT))
        self.wait(2)
        self.play(Write(p_rain_text.scale(
            0.6).to_corner(UR, buff=0.5).shift(LEFT*3)))
        self.wait(2)

        self.play(Write(p_sun_text.scale(0.6).next_to(
            p_rain_text, RIGHT).shift(RIGHT)))

        timer.wait_until("4min 56sec")
        self.wait(2)

        intersection_rain_sun = Intersection(
            rain_circle, sun_circle, color=GREEN_E, fill_opacity=0.4, stroke_width=3)
        fog_circle = Circle(radius=0.5, color=GRAY, fill_opacity=0.7, stroke_width=4).move_to(
            intersection_rain_sun).shift(DOWN*1.5)
        fog_label = MathTex("fog", color=BLACK).move_to(
            fog_circle.get_corner(DR)).scale(0.6)
        fog_group = Group(fog_circle, fog_label).scale(1.2).shift(RIGHT*1.5)
        hail_circle = Circle(radius=0.5, color=TEAL_B,
                             fill_opacity=0.7, stroke_width=4)
        hail_label = MathTex("hail", color=BLACK).move_to(
            hail_circle.get_corner(DR)).scale(0.6)
        hail_group = Group(hail_circle, hail_label).scale(1.2)

        
        self.play(Write(p_rain_sun_text.scale(0.6).move_to(
            p_rain_text.get_corner(DR)).shift(RIGHT*0.7).shift(DOWN*0.4)))
        self.play(intersection_rain_sun.animate.scale(
            0.6).move_to(p_rain_sun_text).shift(DOWN))
        self.play(Indicate(intersection_rain_sun, color=GREEN_D))
        self.play(FadeOut(intersection_rain_sun))
        timer.wait_until("5min 18sec")

        self.wait(4)
        self.play(circles_vdict.animate.scale(1.2).shift(RIGHT*1.5))
        surrounder_circles = SurroundingRectangle(
            circles_vdict, color=GRAY, buff=LARGE_BUFF)

        self.play(Write(surrounder_circles))

        self.wait(4)
        timer.wait_until("5min 44sec")
        self.play(FadeIn(fog_group))

        self.wait(2)
        self.play(FadeOut(fog_group))
        hail_group.next_to(rain_circle, DOWN, buff=-0.5)

        timer.wait_until("5min 50sec")
        self.play(FadeIn(hail_group))
        self.wait(4)
        self.play(FadeOut(hail_group))

        timer.wait_until("6min 8sec")
        self.play(FadeOut(surrounder_circles))

        self.play(circles_vdict.animate.scale(1).shift(LEFT*1.2))
        surrounder_circles = SurroundingRectangle(
            circles_vdict, color=GRAY, buff=MED_SMALL_BUFF)
        self.play(FadeIn(surrounder_circles))

        """
        difference_objects = VGroup(sun_circle,surrounder_circles)
        rain_diff_diagram = Difference(sun_circle,rain_circle,color=GREEN,fill_opacity=1)
        self.play(FadeIn(rain_diff_diagram))
        """
        timer.wait_until("6min 13sec")
        self.play(Write(p_sun_if_rain.scale(0.6).move_to(
            p_rain_sun_text, DOWN).shift(DOWN*1.6).shift(LEFT*2)))

        timer.wait_until("6min 18sec")
        self.play(Write(expression_value_tex.scale(0.6).move_to(
            p_sun_if_rain, RIGHT).shift(UP*0.6).shift(RIGHT*2)),run_time=3)
        self.play(Write(expression_meaning_tex.scale(0.6).move_to(
            p_sun_if_rain, RIGHT).shift(DOWN*0.5).shift(RIGHT*2.3)),run_time=2)
        timer.wait_until("6min 23sec")

        value_arrow = Arrow(p_sun_if_rain, expression_value_tex,
                            color=BLACK, buff=0.2).scale(0.6)
        meaning_arrow = Arrow(
            p_sun_if_rain, expression_meaning_tex, color=BLACK, buff=0.2).scale(0.6)
        arrow_vgroup = VGroup(value_arrow, meaning_arrow)
        self.play(Write(arrow_vgroup))

        timer.wait_until("6min 30sec")
        self.play(Indicate(p_sun_if_rain), color=RED_E, run_time=4)

        timer.wait_until("6min 36sec")
        formula_highlight_1 = SurroundingRectangle(
            p_sun_if_rain[-2], buff=.02, color=BLUE_E, stroke_width=DEFAULT_STROKE_WIDTH/3)
        self.play(Indicate(p_sun_if_rain[-2], color=BLUE_E))
        self.play(Create(Underline(p_sun_if_rain[-2], color=BLUE_E)))

        timer.wait_until("6min 50sec") 
        p_rain_full_tex = MathTex(
            "P(", "rain", ")", "=", "1.0", color=BLUE_E, stroke_width=2)
        self.play(Write(p_rain_full_tex.scale(0.6).move_to(
            p_sun_if_rain, DOWN).shift(DOWN*0.6).shift(LEFT*0.1)),run_time=7)
        self.play(
            Create(Arrow(p_sun_if_rain[-2], p_rain_full_tex, color=BLUE_E).scale(0.3)))

        timer.wait_until("8min 29sec")
        self.play(Write(p_sun_if_rain_longer.scale(0.6).move_to(
            p_sun_if_rain, DOWN).shift(DOWN*2).shift(RIGHT*0.5)),run_time=16)
        timer.wait_until("8min 49sec")
        self.play(Write(p_sun_if_rain_longer_numeric.scale(
            0.6).next_to(p_sun_if_rain_longer, RIGHT)),run_time=12)
        timer.wait_until("9min 1sec")

        self.play(Write(p_rain_if_sun_longer.scale(
            0.6).next_to(p_sun_if_rain_longer, DOWN)),run_time=15)
        timer.wait_until("9min 1sec")
        self.play(Write(p_rain_if_sun_longer_numeric.scale(
            0.6).next_to(p_rain_if_sun_longer, RIGHT)),run_time=6)
        timer.wait_until("9min 28sec")

        p_rain_plus_sun_Indicate_list = Group(
            p_sun_if_rain_longer[2], p_rain_if_sun_longer[2])
        p_sun_if_rain_Indicate_list = Group(
            p_sun_if_rain_longer[0], p_rain_if_sun_longer[0])
        
        self.play(Indicate(p_rain_plus_sun_Indicate_list),
                  color=RED_E, run_time=7)
        
        self.play(Indicate(p_sun_if_rain_Indicate_list),
                  color=RED_E, run_time=6)

        timer.wait_until("9min 47sec")
        self.play(Write(p_rain_plus_sun_longer.scale(0.6).next_to(p_rain_if_sun_longer,DOWN)),run_time=20)

        prob_sun_if_rain_underline = Underline(p_rain_plus_sun_longer[2],color=BLUE_E)
        
        prob_rain_if_sun_underline = Underline(p_rain_plus_sun_longer[6],color=BLUE_E)
        prob_underlines_group = Group(prob_sun_if_rain_underline,prob_rain_if_sun_underline)
        timer.wait_until("10min 11sec")
        self.play(Create(prob_sun_if_rain_underline))
        timer.wait_until("10min 13sec")
        self.play(Create(prob_rain_if_sun_underline))
        timer.wait_until("10min 15sec")
        self.play(FadeOut(prob_rain_if_sun_underline))
        self.play(Write(bayes_with_sun_and_rain.scale(0.6).next_to(p_rain_plus_sun_longer,DOWN).shift(DOWN*0.2)),run_time=11)
        self.wait(3)
        self.play(FadeIn(rain_sun_to_definition.scale(0.6).next_to(bayes_with_sun_and_rain,LEFT).shift(LEFT*0.3)),run_time=3)
        self.play(Write(bayes_definition_tex.scale(0.6).next_to(rain_sun_to_definition,LEFT).shift(LEFT*0.3)),run_time=11)

        timer.wait_until("10min 53sec")
        self.play(Circumscribe(p_rain_full_tex,color=BLUE_B,time_width=3,fade_out=True))
        self.play(Circumscribe(p_rain_full_tex,color=BLUE_B,time_width=3,fade_out=True))
        self.play(Circumscribe(p_rain_full_tex,color=BLUE_B,time_width=3))

        timer.wait_until("11min 10sec")
        self.play(Indicate(p_rain_text,color=BLUE_E))
        
        timer.wait_until("11min 26sec")
        
        #timer.wait_until("17min 38sec")￼
        
