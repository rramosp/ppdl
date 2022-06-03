from __future__ import division
from gzip import WRITE
import logging
from numbers import Integral
import os, sys
from unicodedata import decimal

from numpy import vdot

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
import math

sys.path.insert(0, ".")


config.max_files_cached = 10000
Tex.set_default(color=BLACK)
Tex.set_default(stroke_color=BLACK)
Line.set_default(stroke_color=BLACK)
SingleStringMathTex.set_default(stroke_color=BLACK)
Text.set_default(color=BLACK,stroke_color=BLACK)
CurvedArrow.set_default(color=BLACK, angle=TAU/-4,stroke_width = 2)


class Main(Scene):
    def construct(self):

        video_name = r"bayes theorem continuous part 02"
        #play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-04-continuous-part-02-ES")
       
        self.add_sound(sfile)

        p_z_to_s0 = MathTex(
            "P(", "z", "|", "s_{0}", "=", "22.3m", ")",
            "=",
            "{P(", "s_{0} = 22.3m", "|", "z)", "\cdot", "P(z)",
            "\\over",
            "P(", "s_{0} = 22.3m", ")}", color= BLACK
        )

        p_x = MathTex(
            "P", "(", "x", ")",
            "=",
            "{1",
            "\over",
            "\sigma", "\sqrt{ 2 \pi } }",
            "\cdot",
            " e^{-{1 \over 2}", " ( x- ", "\mu "," )^{2}/ "," \sigma ", "^{2} }", color=BLACK
        )

        timer.wait_until(3)

        self.play(
            FadeIn(p_z_to_s0)
        )

        timer.wait_until(16)

        self.play(
            Indicate(p_z_to_s0[8:12], color=RED_E),
            Indicate(p_z_to_s0[13], color=BLUE_E),
            run_time=3
        )

        timer.wait_until(21)

        self.play(
            p_z_to_s0.animate.scale(0.8).to_edge(UP)
        )

        timer.wait_until(24)

        self.play(
            FadeIn(p_x)
        )

        timer.wait_until(26)
        
        pdf_surrounder = SurroundingRectangle(
            p_x, color=BLUE_E
        )

        pdf_tex = MathTex(
            "PDF"
        ).scale(0.8).next_to(pdf_surrounder, DOWN)


        self.play(
            Create(pdf_surrounder)
        )
        self.play(
            Write(pdf_tex)
        )

        timer.wait_until(31)

        pdf_vdict, pdf_trackers = generate_probability_density_function_graph(median=0)

        line_x = pdf_vdict["axes"].get_vertical_line(pdf_vdict["axes"].input_to_graph_point(1,pdf_vdict["pdf_curve"]), color= RED_E)

        pdf_vdict["vertical_line_x"] = line_x


        x_number_label = MathTex(
        "x", color=BLACK
        ).scale(0.8).move_to(
                    pdf_vdict["axes"].get_axes()[0].get_number_mobject(1),
                )
        
        pdf_vdict["x_label"] = x_number_label.scale(1.5)

        pdf_vdict.scale(0.6).next_to(p_x,DOWN).shift(UP*0.8)

        render_probability_density_function_graph(self,pdf_vdict,pdf_trackers,render_median=False,render_pdf_area_curve=False)

        self.play(
            Write(x_number_label)
        )

        timer.wait_until(38)

        self.play(
            Create(pdf_vdict["vertical_line_x"])
        )

        timer.wait_until(41)

        dot_graph_p_x = Dot(pdf_vdict["axes"].input_to_graph_point(1,pdf_vdict["pdf_curve"]), color=BLACK)

        label_graph_p_x = MathTex("P(x)").scale(0.6).next_to(dot_graph_p_x,UR,buff=0.1)

        self.play(
            Write(dot_graph_p_x),
            Write(label_graph_p_x)
        )

        pdf_vdict["dot_p_x"] = dot_graph_p_x
        pdf_vdict["label_p_x"] = label_graph_p_x


        timer.wait_until(48)

        integral_p_x_graph = MathTex(
            "\int_{-\infty}^{\infty}P(x)dx = 1"
        ).scale(0.8).next_to(label_graph_p_x, LEFT).shift(LEFT*2)

        pdf_vdict["integral_p_x_graph"] = integral_p_x_graph

        self.play(
            Write(integral_p_x_graph)
        )

        timer.wait_until(55)

        line_area_1 = pdf_vdict["axes"].get_vertical_line(pdf_vdict["axes"].input_to_graph_point(-0.8,pdf_vdict["pdf_curve"]), color= BLUE_E)
        line_area_2 = pdf_vdict["axes"].get_vertical_line(pdf_vdict["axes"].input_to_graph_point(-0.3,pdf_vdict["pdf_curve"]), color= BLUE_E)

        pdf_vdict["line_area_1"] = line_area_1
        pdf_vdict["line_area_2"] = line_area_2

        area_pdf = pdf_vdict["axes"].get_area(pdf_vdict["pdf_curve"], [-0.8, -0.3] , color=BLUE_E, opacity=0.3)

        pdf_vdict["area_pdf"] = area_pdf

        self.play(
            Create(line_area_1),
            Create(line_area_2)
        )
        self.play(
            Write(area_pdf)
        )

        pdf_vdict["axes"] = pdf_vdict["axes"].get_axes()[0]

        del pdf_vdict["area_under_curve"]
        del pdf_vdict["zero_label"]
        del pdf_vdict["median_label"]

        timer.wait_until("1min 4sec")

        self.play(
            FadeOut(pdf_vdict)
        )

        self.play(
            Uncreate(pdf_surrounder),
            FadeOut(pdf_tex)
        )

        timer.wait_until("1min 17sec")

        p_z_copy = p_z_to_s0[13].copy()

        self.play(
            p_z_copy.animate.move_to(ORIGIN).shift(DOWN*2).shift(LEFT*2)
        )

        timer.wait_until("1min 24sec")

        tex_besides_p_z = MathTex(
            "\\rightarrow", "N(","20",",", "10", ")", color=BLACK
        ).scale(0.8).next_to(p_z_copy,RIGHT, buff=0.1)

        self.play(
            Write(tex_besides_p_z)
        )

        timer.wait_until("1min 41sec")

        pdf_vdict, pdf_trackers = generate_probability_density_function_graph(median=4,x_range=[0,8,1])
        curve_1 = pdf_vdict["axes"].plot(lambda x: (1/64)*(8 * x - x ** 2), x_range=[0, 8], color=RED_E)
        
        pdf_vdict["curve"] = curve_1

        pdf_vdict.scale(0.3).next_to(tex_besides_p_z,RIGHT).shift(UP*0.5)

        render_probability_density_function_graph(self,pdf_vdict,pdf_trackers,render_median=False,render_pdf_area_curve=False)

        timer.wait_until("1min 43sec")        

        self.play(
            Create(curve_1)
        )


        timer.wait_until("1min 50sec")

        tex_one = MathTex("1", color = BLACK).scale(0.8).move_to(tex_besides_p_z[-2])

        self.play(
            FadeOut(tex_besides_p_z[-2]),
            FadeIn(tex_one)
        )


        timer.wait_until("1min 54sec")
        self.play(
            pdf_trackers["sigma"].animate.set_value(0.5), run_time=3,
            rate_func=rate_functions.smooth
        )

        timer.wait_until("1min 59sec")

        self.play(
            Uncreate(pdf_vdict["curve"]),
            Uncreate(pdf_vdict["axes"].get_axes()[0]),
            Uncreate(pdf_vdict["pdf_curve"])
        )

        timer.wait_until("2min 1sec")

        self.play(
            FadeOut(tex_besides_p_z),
            FadeOut(tex_one)
        )

        tex_besides_p_z = MathTex(
            "\\rightarrow", "N(","20",",", "3", ")", color=BLACK
        ).scale(0.8).next_to(p_z_copy,RIGHT, buff=0.1)

        self.play(
            FadeIn(tex_besides_p_z)
        )

        timer.wait_until("2min 11sec")

        updating_animation(p_x,self)

        timer.wait_until("2min 15sec")

        updating_animation(
            [ tex_besides_p_z[2], p_x[-4] ],
            self,
            color=RED_E
        )

        timer.wait_until("2min 18sec")

        updating_animation(
            [ tex_besides_p_z[-2], p_x[7], p_x[-2] ],
            self,
            GREEN_E
        )

        timer.wait_until("2min 22sec")

        updating_animation(
            [ p_x, p_z_to_s0[13] ],
            self,
            BLUE_E
        )

        timer.wait_until("2min 29sec")

        

        self.play(
            p_x.animate.to_corner(UL),
            p_z_to_s0.animate.to_corner(UR)
        )
        self.play(
            FadeOut(p_z_copy,tex_besides_p_z)
        )

        updating_animation(p_z_to_s0[8:12], self, ORANGE)

        p_s0_z = MathTex(
            "P(", "s_0|z", ")", "\\rightarrow", "N(", "z", "," ,"1", ")" , "(", "s_0 = 22.3", ")"
        ).scale(0.8)
        
        timer.wait_until("2min 41sec")

        self.play(
            Write(p_s0_z[0:3])
        )

        timer.wait_until("2min 44sec")

        self.play(
            Write(p_s0_z[4]),
        )
        self.play(
            Write(p_s0_z[3]),
        )

        timer.wait_until("2min 47sec")

        self.play(
            Write(p_s0_z[5]),
        )

        timer.wait_until("2min 50sec")

        self.play(
            Write(p_s0_z[6:9])
        )

        timer.wait_until("3min 1sec")

        self.play(
            Write(p_s0_z[9:])
        )

        timer.wait_until("3min 4sec")

        underline_p_s0 = Underline(p_s0_z[4:], color=RED_E)

        self.play(
            Write(underline_p_s0)
        )

        timer.wait_until("3min 16sec")

        updating_animation(
            [ p_s0_z[5], p_x[-4] ],
            self,
            RED_E
        )

        timer.wait_until("3min 20sec")

        updating_animation(
            [ p_s0_z[-3:], p_x[-5] ],
            self,
            ORANGE
        )

        timer.wait_until("3min 24sec")

        updating_animation(
            [ p_s0_z[7], p_x[7], p_x[-2] ],
            self,
            GREEN_E
        )

        timer.wait_until("3min 30sec")

        vgroup_p_s0_z = VGroup(p_s0_z, underline_p_s0)

        self.play(
            vgroup_p_s0_z.animate.shift(UP*2)
        )

        timer.wait_until("3min 32sec")

        big_frac_p_z_s0 = MathTex(
           "P(z|s_0=22.3m)", "=",

            "{ {1 \over1 \cdot ", " \sqrt{2 \pi} }",

            "\cdot e^{ ", "-\\frac{1}{2} (22.3-z)^2/1^2} ",

            "\cdot ", "{\\frac{1}{3 \cdot", " \sqrt{2 \pi} }",

            "\cdot e^{ ", "-\\frac{1}{2}(z-20)^2/3^2} }",

            "\over",

            "\int[ ","{ {1 \over 1 \cdot ", "\sqrt{2 \pi} } }", 

            "\cdot e^{ ", "-\\frac{1}{2} (22.3-z)^2/1^2}",

            "{\\frac{1}{3\cdot ", "\sqrt{2 \pi} }", 

            "\cdot e^{ "," -\\frac{1}{2}(z-20)^2/3^2} }", 

            "]dz}"
        )


        self.play(
            FadeIn(big_frac_p_z_s0)
        )


        timer.wait_until("3min 40sec")
        
        updating_animation(
            big_frac_p_z_s0[13:21],
            self
        )

        updating_animation(
            big_frac_p_z_s0[2:11],
            self
        )

        timer.wait_until("3min 52sec")

        surrounder_likelihood = SurroundingRectangle(big_frac_p_z_s0[2:6], color=RED_E)
        surrounder_prior = SurroundingRectangle(big_frac_p_z_s0[7:11], color=GREEN_E)

        likelihood_label = MathTex("likelihood").scale(0.8).next_to(surrounder_likelihood,UP,buff=SMALL_BUFF)
        prior_label = MathTex("prior").scale(0.8).next_to(surrounder_prior,UP,buff=SMALL_BUFF)

        self.play(
            Create(surrounder_likelihood)
        )

        self.play(
            Write(likelihood_label)
        )

        timer.wait_until("3min 55sec")

        self.play(
            Create(surrounder_prior)
        )

        self.play(
            Write(prior_label)
        )

        timer.wait_until("3min 57sec")

        updating_animation(
            big_frac_p_z_s0[13:21],
            self
        )

        timer.wait_until("4min")

        self.play(
            Uncreate(surrounder_likelihood),
            Uncreate(surrounder_prior),
            FadeOut(prior_label),
            FadeOut(likelihood_label)
        )

        timer.wait_until("4min 3sec")

        self.play(
            Indicate(big_frac_p_z_s0[5], color=RED_E),
            Indicate(big_frac_p_z_s0[16], color=RED_E),
            run_time=2
        )

        self.play(
            Indicate(big_frac_p_z_s0[10], color=GREEN_E),
            Indicate(big_frac_p_z_s0[20], color=GREEN_E),
            run_time=4
        )

        timer.wait_until("4min 10sec")

        updating_animation(
            big_frac_p_z_s0[2:11],
            self
        )     

        timer.wait_until("4min 22sec")

        updating_animation(
            big_frac_p_z_s0[12:],
            self,
            color=RED_E
        )

        timer.wait_until("4min 37sec")

        underline_leftside = Underline(big_frac_p_z_s0[0],color=BLUE_E)

        self.play(
            Write(underline_leftside)
        )

        timer.wait_until("5min 4sec")

        updating_animation(
            [big_frac_p_z_s0[2:4], big_frac_p_z_s0[7:9]],
            self,
        )

        timer.wait_until("5min 7sec")

        updating_animation(
            [big_frac_p_z_s0[3], big_frac_p_z_s0[8]],
            self,
            color=RED_E
        )

        timer.wait_until("5min 12sec")

        updating_animation(
            [big_frac_p_z_s0[10], big_frac_p_z_s0[5]],
            self,
            color=GREEN_E
        )

        timer.wait_until("5min 32sec")

        self.play(
            FadeOut(*self.mobjects)
        )

        s0 = MathTex("S_0")
        s1 = MathTex("S_1")
        s2 = MathTex("S_2")
        s_i = MathTex("S_i")
        dotted_line_s_i = DashedLine(start=s2.get_edge_center(DOWN), end=DOWN, dashed_ratio=0.3)

        column_s_i_vgroup = VGroup(s0,s1,s2,dotted_line_s_i,s_i)

        column_s_i_vgroup.arrange(DOWN)

        self.play(Write(column_s_i_vgroup))

        timer.wait_until("5min 42sec")

        posterior_tex = MathTex("posterior").scale(0.8).next_to(s0,RIGHT)
        prior_tex = MathTex("prior").scale(0.8).next_to(s1,RIGHT)
        curved_arrow_1 = CurvedArrow(posterior_tex.get_edge_center(DOWN), prior_tex.get_edge_center(RIGHT))
        curved_arrow_2 = CurvedArrow(prior_tex.get_edge_center(DOWN), s2.get_edge_center(RIGHT))
        curved_arrow_3 = CurvedArrow(curved_arrow_2.get_edge_center(DOWN), dotted_line_s_i.get_edge_center(RIGHT))
        curved_arrow_4 = CurvedArrow(curved_arrow_3.get_edge_center(DOWN), s_i.get_edge_center(RIGHT))

        curved_arrow_1.pop_tips()
        curved_arrow_2.pop_tips()
        curved_arrow_3.pop_tips()
        curved_arrow_4.pop_tips()
        
        curved_arrow_1.add_tip(tip_length=0.175)
        curved_arrow_2.add_tip(tip_length=0.175)
        curved_arrow_3.add_tip(tip_length=0.175)
        curved_arrow_4.add_tip(tip_length=0.175)

        self.play(
            Write(posterior_tex)
        )

        timer.wait_until("5min 47sec")

        self.play(
            Create(curved_arrow_1)
        )
        self.play(
            Write(prior_tex)
        )
        
        self.play(
            Create(curved_arrow_2)
        )
        self.play(
            Create(curved_arrow_3)
        )
        self.play(
            Create(curved_arrow_4)
        )

        column_s_i_vgroup.add(posterior_tex, prior_tex, curved_arrow_1, curved_arrow_2, curved_arrow_3, curved_arrow_4)

        self.play(
            column_s_i_vgroup.animate.to_edge(LEFT)
        )
        
        

        
        timer.wait_until("5min 52sec")

        simple_p_z_s0 = MathTex("P(z|s_0)")

        self.play(
            Write(simple_p_z_s0)
        )

        timer.wait_until("6min")

        self.play(
            simple_p_z_s0.animate.shift(UP)
        )

        simple_s1 = MathTex("s_1").next_to(simple_p_z_s0,DOWN)

        timer.wait_until("6min 5sec")

        self.play(
            simple_p_z_s0.animate.shift(UP),
            simple_s1.animate.shift(UP),
        )

        p_z_s1 = MathTex(
            "P(z|s_1)", "=", "{P(s_1|z)", "\cdot ", "P(z|s_0) ", "\over ", "P(s_1)}"
        )

        self.play(
            Write(
                p_z_s1[0]
            )
        )

        self.play(
            Write(p_z_s1[1:3])
        )

        timer.wait_until("6min 12sec")

        self.play(
            Write(p_z_s1[4])
        )

        self.play(
            Write(p_z_s1[3])
        )

        updating_animation(
            [simple_p_z_s0, p_z_s1[4]],
            self,
        )

        timer.wait_until("6min 22sec")

        self.play(
            Write(p_z_s1[5:])
        )

        timer.wait_until("6min 30sec")
        
        updating_animation(
            [posterior_tex, simple_p_z_s0],
            self,
            color=RED_E
        )

        updating_animation(
            [prior_tex, p_z_s1[4]],
            self,
            color=GREEN_E
        )

        timer.wait_until("6min 39sec")

        p_z_si = MathTex(
            "P(z|s_i)", "=", "{P(s_i|z)", "\cdot ", "P(z|s_{i-1}) ", "\over ", "P(s)}"
        ).next_to(p_z_s1,DOWN)

        self.play(
            FadeIn(p_z_si,shift=UP)
        )

        timer.wait_until("6min 42sec")

        self.play(
            ReplacementTransform(p_z_s1,p_z_si)
        )

        timer.wait_until("6min 45sec")

        self.play(
            p_z_si.animate.shift(UP)
        )

        timer.wait_until("6min 52sec")

        pdf_vdict, pdf_trackers = generate_probability_density_function_graph(median=0,x_range=[-4,4,1],initial_sigma=0.5)
        pdf_vdict.scale(0.3).to_edge(DOWN).shift(UP*0.5)
        pdf_vdict["median_label"].scale(2)

        self.play(
            Write(
                MathTex("P(z)").shift(DOWN*3).shift(LEFT*3)
            )
        )

        timer.wait_until("6min 55sec")

        render_probability_density_function_graph(self,pdf_vdict,pdf_trackers,render_median=True,render_pdf_area_curve=False)

        timer.wait_until("6min 59sec")

        self.play(
            pdf_trackers["sigma"].animate.set_value(1), run_time=3,
            rate_func=rate_functions.smooth
        )

        timer.wait_until("7min 2sec")

        self.play(
            pdf_trackers["shifter_x_axis_pdf"].animate.set_value(-2),
            pdf_trackers["sigma"].animate.set_value(0.5), run_time=3,
            rate_func=rate_functions.smooth
        )

        timer.wait_until("7min 9sec")

        self.play(
            pdf_trackers["shifter_x_axis_pdf"].animate.set_value(0), 
            rate_func=rate_functions.smooth
        )

        timer.wait_until("7min 11sec")

        updating_animation(
            p_z_si,
            self,
            RED_E
        )

        timer.wait_until("7min 31sec")

        updating_animation(
            prior_tex,
            self,
            BLUE_E
        )

        timer.wait_until("7min 33sec")

        self.play(
            Write(
                MathTex("std = 1").shift(DOWN*3).shift(LEFT*3).shift(DOWN*0.5)
            )
        )
        
        timer.wait_until("7min 42sec")

        updating_animation(
            p_z_si[-1],
            self,
            ORANGE
        )

        ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)