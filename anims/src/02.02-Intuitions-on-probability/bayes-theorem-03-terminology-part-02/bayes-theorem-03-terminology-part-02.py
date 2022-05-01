from __future__ import division
from gzip import WRITE
import logging
from multiprocessing.connection import wait
import os, sys
from tkinter import Image
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
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-03-terminology-part-02-ES")
        
        self.add_sound(sfile)
        

        bayes_p_disease_to_positive = MathTex(
            "P","(","disease","|","positive", ")" , "=", 
            "{P(","positive", "|", "disease", ")", "\cdot", "P(disease)",
            "\\over", "P(", "positive", ")}" , color= BLACK
        ).scale(1).shift(UP)
        bayes_p_disease_to_positive.set_color_by_tex("positive",RED_E)


        p_disease_to_pos_fracc = MathTex(
            "P(disease|", "positive",") = ", "{P(", "positive", "|disease)", "\\cdot" , "P(disease)",
            "\\over",
            "P(" , "positive", "|disease)", "\\cdot", "P(disease) " , " + ", "P(", "positive", "|" ,"\lnot" ,"disease)", "\\cdot" , "P(", "\lnot" ,"disease)}"
            , color= BLACK
        ).scale(0.8)
        p_disease_to_pos_fracc.set_color_by_tex("positive", RED_E)

        p_disease_to_pos_fracc_copy = p_disease_to_pos_fracc.copy()

        posterior_brace = Brace(bayes_p_disease_to_positive[:6],direction=UP,color=BLACK)

        posterior_tex = MathTex("Posterior", color=BLACK).scale(0.8).next_to(posterior_brace,UP)
        prior_brace = Brace(bayes_p_disease_to_positive[-5], color=BLACK, direction=UP)
        prior_tex = MathTex("Prior", color=BLACK).scale(0.8).next_to(prior_brace,UP)
        likelihood_brace = Brace(bayes_p_disease_to_positive[7:12],color=BLACK,direction=UP)
        likelihood_tex = MathTex("Likelihood", color=BLACK).scale(0.7).next_to(likelihood_brace,UP)
        norm_factor_brace = Brace(bayes_p_disease_to_positive[-3:],direction=DOWN, color=BLACK )
        norm_factor_tex = MathTex("Normalization \hspace{0.2cm} Factor", color=BLACK).scale(0.8).scale(0.8).next_to(norm_factor_brace,DOWN)
        

        self.play(Write(bayes_p_disease_to_positive))
        self.play(FadeIn(posterior_brace), FadeIn(prior_brace), Write(likelihood_brace), FadeIn(norm_factor_brace) )
        self.play(Write(posterior_tex), Write(prior_tex), Write(likelihood_tex), Write(norm_factor_tex))
        
        vgroup_bayes_p_disease_to_positive = VGroup(bayes_p_disease_to_positive,
                                            posterior_brace,posterior_tex, prior_brace , prior_tex,
                                            likelihood_brace, likelihood_tex, norm_factor_brace, norm_factor_tex )

        test_1_tex = MathTex(r"test 1: ", "positive", color=BLACK).scale(0.7).shift(LEFT*6).shift(UP*1)
        test_1_tex.set_color_by_tex("positive", RED_E)

        p_d_prior = MathTex("P(disease)=", "0.01", color=BLACK).scale(0.7).next_to(test_1_tex,RIGHT).shift(RIGHT*0.5)
        p_d_prior_copy_2 = p_d_prior.copy()

        test_1_posterior = MathTex("P(disease|", "positive", ")", "=", "0.147").scale(0.7).next_to(p_d_prior,DOWN).align_to(p_d_prior,LEFT)
        test_1_posterior.set_color_by_tex("positive", RED_E)
        test_1_posterior_copy_3 =test_1_posterior.copy()
        
        test_2_tex = MathTex(
            r"test 2: ", " positive", color=BLACK
        ).scale(0.7).to_edge(RIGHT,buff=MED_SMALL_BUFF).shift(UP)
        test_2_tex.set_color_by_tex("positive",RED_E)



        self.play(vgroup_bayes_p_disease_to_positive.animate.scale(0.7).shift(UP*1.8))
        bayes_p_disease_to_positive_copy = bayes_p_disease_to_positive.copy()

        timer.wait_until(10)

        self.play(Write(test_1_tex))

        timer.wait_until(17)

        self.play(Write(p_d_prior))

        timer.wait_until(19)   

        updating_animation(prior_tex,self)
        updating_animation(p_d_prior[-1],self)

        timer.wait_until(27)

        updating_animation(posterior_tex,self)

        timer.wait_until(31)

        self.play(Write(test_1_posterior))

        timer.wait_until(47)

        self.play(Indicate(p_d_prior, color=RED_E, run_time=3, scale_factor=1.05))

        timer.wait_until("1min 7sec")

        self.play(Write(test_2_tex))

        timer.wait_until("1min 26sec")

        p_d_prior_copy =  p_d_prior.copy()
        test_1_posterior_copy = test_1_posterior.copy()

        post_obs_1_tex = MathTex("posterior \hspace{0.2cm} observation \hspace{0.2cm} 1", color=BLACK).scale(0.7).next_to(test_2_tex,LEFT).shift(LEFT*0.5)
        prior_obs_2_tex = MathTex("prior \hspace{0.2cm} observation \hspace{0.2cm} 2", color=BLACK).scale(0.7).next_to(post_obs_1_tex,DOWN).shift(DOWN*0.3)

        post_obs1_to_prior_obs_2_arrow = Arrow(start=post_obs_1_tex.get_edge_center(DOWN),end=prior_obs_2_tex.get_edge_center(UP),color=BLACK,buff=0.1)

        
        self.play(ReplacementTransform(p_d_prior_copy,post_obs_1_tex))

        timer.wait_until("1min 34sec")
        self.play(Write(post_obs1_to_prior_obs_2_arrow))
        self.play(ReplacementTransform(test_1_posterior_copy, prior_obs_2_tex))

        timer.wait_until("1min 42sec")

        p_disease_to_pos_fracc.to_edge(DOWN,buff=MED_LARGE_BUFF).shift(UP*2)

        self.play(ReplacementTransform(bayes_p_disease_to_positive_copy, p_disease_to_pos_fracc))

        timer.wait_until("1min 47sec")

        updating_animation(p_disease_to_pos_fracc[7],self)

        timer.wait_until("1min 50sec")

        updating_animation(p_d_prior[-1],self)

        timer.wait_until("1min 53sec")

        updating_animation(test_1_posterior,self)
        
        test_1_posterior_copy_2 = test_1_posterior.copy()

        timer.wait_until("2min 3sec")

        self.play(test_1_posterior_copy_2[-1].animate.scale(0.8).next_to(p_disease_to_pos_fracc[7],UP,buff=0.1))

        timer.wait_until("2min 14sec")

        self.play(Indicate(p_disease_to_pos_fracc[9:12], color=RED_E, scale_factor=1.05),
                 Indicate( p_disease_to_pos_fracc[3:6], color=RED_E, scale_factor=1.05),  run_time=4
                 )
    
        timer.wait_until("2min 18sec")

        self.play(Indicate(p_disease_to_pos_fracc[-9:-3], color=GREEN_E, scale_factor=1.05 ,run_time=3))

        timer.wait_until("2min 21sec")

        label_1 = MathTex("0.85",color=BLACK).scale(0.5).next_to(p_disease_to_pos_fracc[3:6], UP, buff=0.1)
        label_2 = MathTex("0.85",color=BLACK).scale(0.5).next_to(p_disease_to_pos_fracc[9:12], DOWN, buff=0.1)
        label_3 = MathTex("0.05",color=BLACK).scale(0.5).next_to(p_disease_to_pos_fracc[-8:-3], DOWN, buff=0.1)
        label_4 = MathTex("0.147",color=BLACK).scale(0.5).next_to(p_disease_to_pos_fracc[13], DOWN, buff=0.1)
        label_5 = MathTex("(1-0.147)",color=BLACK).scale(0.5).next_to(p_disease_to_pos_fracc[-3:], DOWN, buff=0.1)

        self.play(Write(label_1))
        self.play(Write(label_2))

        timer.wait_until("2min 26sec")
        self.play(Write(label_3))

        timer.wait_until("2min 37sec")

        self.play(Write(label_4))

        timer.wait_until("2min 40sec")

        self.play(Write(label_5))

        timer.wait_until("2min 46sec")

        vgroup_posterior_to_prior = VGroup(post_obs_1_tex, prior_obs_2_tex, post_obs1_to_prior_obs_2_arrow)

        updating_animation(vgroup_posterior_to_prior, self)

        timer.wait_until("2min 56sec")

        normalization_brace = Brace(p_disease_to_pos_fracc[9:],color=BLACK,buff=0.2)
        result_normalization_tex = MathTex("0.1676", color=BLACK).scale(0.6).next_to(normalization_brace,DOWN)

        self.play(FadeIn(normalization_brace))

        timer.wait_until("2min 59sec")

        self.play(Write(result_normalization_tex))

        timer.wait_until("3min 2sec")

        result_complete_tex = MathTex(
            "P(disease|", "positive", ")= ", " 0.746", color=BLACK
        ).scale(0.8).next_to(p_disease_to_pos_fracc,DOWN).shift(DOWN*0.5).align_to(p_disease_to_pos_fracc,LEFT)
        result_complete_tex.set_color_by_tex("positive", RED_E)
        
        self.play(FadeIn(result_complete_tex[0:-1]))

        timer.wait_until("3min 4sec")

        vgroup_labels_copy = VGroup(label_1,label_2,label_3,label_4,label_5, test_1_posterior_copy_2[-1]).copy()

        self.play(ReplacementTransform(vgroup_labels_copy,result_complete_tex[-1]))
        
        timer.wait_until("3min 23sec")

        obs_1_prior_tex = MathTex("0.01",color=BLACK).scale(0.8).to_edge(DOWN,MED_SMALL_BUFF).shift(LEFT)
        obs_1_posterior_tex = MathTex("0.147", color=BLACK).scale(0.8).next_to(obs_1_prior_tex,RIGHT).shift(RIGHT*0.5)
        obs_1_arrow = Arrow(start=obs_1_prior_tex.get_edge_center(RIGHT), end= obs_1_posterior_tex.get_edge_center(LEFT),buff=0.1)

        self.play(Write(obs_1_prior_tex))

        timer.wait_until("3min 29sec")

        self.play(Write(obs_1_posterior_tex))
        self.play(Write(obs_1_arrow))

        timer.wait_until("3min 33sec")

        tilted_first_obs_tex = MathTex("obs \hspace{0.01cm} 1").scale(0.5).rotate(PI/3).next_to(obs_1_arrow,UP,buff=0.1)

        self.play(FadeIn(tilted_first_obs_tex))

        timer.wait_until("3min 36sec")

        obs_2_result_tex = MathTex("0.746", color=BLACK).scale(0.8).next_to(obs_1_posterior_tex,RIGHT).shift(RIGHT*0.5)
        obs_2_arrow = Arrow(start=obs_1_posterior_tex.get_edge_center(RIGHT), end= obs_2_result_tex.get_edge_center(LEFT),buff=0.1)
        tilted_second_obs_tex = MathTex("obs \hspace{0.01cm} 2").scale(0.5).rotate(PI/3).next_to(obs_2_arrow,UP,buff=0.1)

        self.play(Write(obs_2_arrow))
        self.play(FadeIn(tilted_second_obs_tex))

        timer.wait_until("3min 44sec")

        self.play(FadeIn(obs_2_result_tex))

        timer.wait_until("3min 50sec")

        obs_n_tex = MathTex(
            "\hspace{0.2cm} \cdot \hspace{0.2cm} \cdot \hspace{0.2cm} \cdot",color=BLACK
        ).next_to(obs_2_result_tex,RIGHT).shift(RIGHT*0.5)

        obs_n_arrow = Arrow(start=obs_2_result_tex.get_edge_center(RIGHT), end= obs_n_tex.get_edge_center(LEFT),buff=0.1)
        tilted_n_obs_tex = MathTex("obs \hspace{0.01cm} n ").scale(0.5).rotate(PI/3).next_to(obs_n_arrow,UP,buff=0.1)

        self.play(Write(obs_n_tex))
        self.play(FadeIn(obs_n_arrow))
        self.play(Write(tilted_n_obs_tex))


        timer.wait_until("4min 18sec")

        updating_animation(p_disease_to_pos_fracc[7], self)


        timer.wait_until("4min 29sec")

        self.play(
            Indicate(tilted_first_obs_tex, color=RED_E),
            Indicate(tilted_second_obs_tex, color=RED_E),
            Indicate(tilted_n_obs_tex, color=RED_E),
            run_time=5
        )

        timer.wait_until("4min 36sec")

        self.play(Indicate(p_disease_to_pos_fracc[9:12], color=RED_E, scale_factor=1.05),
                Indicate( p_disease_to_pos_fracc[3:6], color=RED_E, scale_factor=1.05),
                Indicate(p_disease_to_pos_fracc[-9:-3], color=GREEN_E, scale_factor=1.05),
                run_time=4
        )


        timer.wait_until("4min 46sec")

        self.play(FadeOut(*self.mobjects))

        timer.wait_until("4min 48sec")

        p_pos_d_TP = MathTex(
            "P(", "positive", "|", "disease)" , "=", "TP", color=BLACK
        ).scale(1)
        p_pos_d_TP.set_color_by_tex("positive", RED_E)


        self.play(Write(p_pos_d_TP[:-2]))

        timer.wait_until("5min 1sec")

        self.play(Write(p_pos_d_TP[-2:]))

        timer.wait_until("5min 8sec")

        

        p_pos_not_d_FPR = MathTex(
            "P(", "positive", "|", "\lnot" ,"disease)" ,"=", "FPR", color=BLACK
        ).scale(1).next_to(p_pos_d_TP,DOWN)
        p_pos_not_d_FPR.set_color_by_tex("positive", RED_E)

        self.play(Write(p_pos_not_d_FPR[:-2], run_time=5))

        timer.wait_until("5min 17sec")

        self.play(Write(p_pos_not_d_FPR[-2:]))

        timer.wait_until("5min 40sec")

        arrow_decrease_FPR = Arrow(
            start=ORIGIN, end=DOWN,
            stroke_width=12, max_tip_length_to_length_ratio=0.5,
            color=GREEN_E
        ).scale(0.5).next_to(p_pos_not_d_FPR,RIGHT)

        arrow_increase_TP = Arrow(
            start=ORIGIN, end=UP,
            stroke_width=12, max_tip_length_to_length_ratio=0.5,
            color=RED_E
        ).scale(0.5).next_to(p_pos_d_TP,RIGHT).align_to(arrow_decrease_FPR,LEFT)



        self.play(Write(arrow_increase_TP))

        updating_animation(p_pos_d_TP[-1], self, color=RED_E)

        timer.wait_until("5min 48sec")

        

        self.play(Write(arrow_decrease_FPR))

        updating_animation(p_pos_not_d_FPR[-1], self, color=GREEN_E)

        timer.wait_until("5min 58sec")

        self.play(
            VGroup(
                p_pos_d_TP,
                p_pos_not_d_FPR, arrow_decrease_FPR,
                arrow_increase_TP
            ).animate.to_corner(UL)
        )

        timer.wait_until("6min 4sec")

        equivalence_TP_tex = MathTex(
            "= 1-", "FN", "=", "1-","P(", "negative", "|" ,"disease)"
        ).scale(1).next_to(arrow_increase_TP,RIGHT)
        equivalence_TP_tex.set_color_by_tex("negative", GREEN_E)

        self.play(Write(equivalence_TP_tex[:2]))

        timer.wait_until("6min 8sec")

        self.play(Write(equivalence_TP_tex[2:]))

        timer.wait_until("6min 30sec")

        updating_animation(equivalence_TP_tex[1],self)

        timer.wait_until("6min 38sec")

        updating_animation(p_pos_not_d_FPR[-1], self)
        
        timer.wait_until("6min 56sec")

        self.play(
            VGroup(equivalence_TP_tex,p_pos_d_TP,
                p_pos_not_d_FPR, arrow_decrease_FPR,arrow_increase_TP
            ).animate.to_corner(UL)
        )

        p_disease_to_pos_fracc_copy.to_edge(DOWN)

        self.play(FadeIn(p_disease_to_pos_fracc_copy))

        timer.wait_until("7min 3sec")

        updating_animation(equivalence_TP_tex[1],self, color=RED_E)

        timer.wait_until("7min 7sec")

        updating_animation(p_pos_d_TP[-1] ,self, color=RED_E )

        timer.wait_until("7min 11sec")

        self.play(
            Indicate(p_disease_to_pos_fracc_copy[3:6], color=RED_E,scale_factor=1.05),
            Indicate(p_disease_to_pos_fracc_copy[9:12], color=RED_E,scale_factor=1.05),
            run_time=5
        )

        timer.wait_until("7min 27sec")

        self.play(
            Write(Underline(p_disease_to_pos_fracc_copy[9:14], color=RED_E))
        )
        
        timer.wait_until("7min 29sec")

        self.play(
            Write(Underline(p_disease_to_pos_fracc_copy[15:], color=GREEN_E))
        )

        timer.wait_until("7min 41sec")
                    
                    
        fnr_image = ImageMobject(find_imgfile("p_cancer_to_pos_FNR")).scale(2).to_edge(LEFT).shift(RIGHT)
        fpr_image = ImageMobject(find_imgfile("p_cancer_to_pos_FPR")).scale(2).to_edge(RIGHT).shift(LEFT)

        test_1_posterior_copy_3.to_corner(UR).shift(DOWN)
        p_d_prior_copy_2.next_to(test_1_posterior_copy_3,DOWN)

        self.play(Write(p_d_prior_copy_2))

        timer.wait_until("7min 49sec")

        self.play(Write(test_1_posterior_copy_3[:3]))

        timer.wait_until("7min 52sec")

        self.play(Write(test_1_posterior_copy_3[3:]))

        timer.wait_until("7min 54sec")

        arrow_decrease_FNR_graph = Arrow(
            start=fnr_image.get_corner(DR),
            end= fnr_image.get_corner(DL), color=BLUE_E
        ).next_to(fnr_image,DOWN,buff=0.1)

        self.play(FadeIn(fnr_image))

        timer.wait_until("7min 58sec")

        self.play(Write(arrow_decrease_FNR_graph))

        timer.wait_until("8min 4sec")

        updating_animation(p_pos_d_TP[-1], self, color=RED_E)

        timer.wait_until("8min 10sec")

        self.play(
            Write(
                Dot(
                    fnr_image.get_corner(DR),
                    color=RED_E
                ).shift(LEFT*0.28).shift(UP*0.6)
            )
        )

        timer.wait_until("8min 12sec")

        self.play(Indicate(arrow_decrease_FNR_graph,color=BLUE_E),run_time=4)

        timer.wait_until("8min 17sec")

        self.play(
            Write(
                Dot(
                    fnr_image.get_corner(UL),
                    color=RED_E
                ).shift(RIGHT*0.72).shift(DOWN*0.45)
            )
        )

        timer.wait_until("8min 25sec")

        self.play(
            Write(
                Circle(
                    color=RED_E,
                    fill_opacity=0.2
                ).scale(0.3).move_to(fnr_image.get_corner(DL)).shift(RIGHT*0.75).shift(UP*0.5)
            )
        )

        timer.wait_until("8min 31sec")

        updating_animation(p_pos_not_d_FPR[-1],self ,color=GREEN_E)

        timer.wait_until("8min 38sec")

        self.play(Indicate(p_disease_to_pos_fracc_copy[-9:-4],scale_factor=1.05, color=BLUE_E), run_time=8)

        timer.wait_until("8min 51sec")

        self.play(Indicate(p_disease_to_pos_fracc_copy[:3],scale_factor=1.05,color=BLUE_E), run_time=5)

        timer.wait_until("8min 57sec")

        self.play(FadeIn(fpr_image))

        timer.wait_until("9min 1sec")

        arrow_decrease_FPR_graph = Arrow(
            start=fpr_image.get_corner(DR),
            end= fpr_image.get_corner(DL), color=BLUE_E
        ).next_to(fpr_image,DOWN,buff=0.1)

        self.play(
            Write(
                Dot(
                    fpr_image.get_corner(DR),
                    color=GREEN_E,
                    fill_opacity=1
                ).shift(LEFT*0.2).shift(UP*0.45)
            )
        )


        timer.wait_until("9min 7sec")

        self.play(Write(arrow_decrease_FPR_graph))

        timer.wait_until("9min 15sec")

        self.play(
            Write(
                Circle(
                    color=GREEN_E,
                    fill_opacity=0.2
                ).scale(0.3).move_to(fpr_image.get_corner(UL)).shift(RIGHT*0.6).shift(DOWN*0.5)
            )
        )

        timer.wait_until("9min 24sec")

        zero_tex =  MathTex(
                        "0",
                        color=BLACK
                    ).scale(0.6).next_to(p_disease_to_pos_fracc_copy[-9:],DOWN)

        self.play(
            Write(
                zero_tex
            )
        )



        self.play(
            Indicate(
                    p_disease_to_pos_fracc_copy[-9:],
                    color=BLUE_E,
                    scale_factor=1.1
            ), run_time=3
        )

        timer.wait_until("9min 28sec")

        cancel_line_1 = Line(
                            start=p_disease_to_pos_fracc_copy[9:14].get_corner(DL),
                            end=p_disease_to_pos_fracc_copy[9:14].get_corner(UR)
                        )
        cancel_line_2 = Line(
                            start=p_disease_to_pos_fracc_copy[3:8].get_corner(DL),
                            end=p_disease_to_pos_fracc_copy[3:8].get_corner(UR)
                        )

        self.play(Write(cancel_line_1), Write(cancel_line_2))

        timer.wait_until("9min 40sec")

        updating_animation(fpr_image,self,color=GREEN_E)

        timer.wait_until("9min 43sec")

        updating_animation(fnr_image,self,color=RED_E)

        timer.wait_until("9min 52sec")

        self.play(Write(MathTex("\ll", color= BLACK).scale(2)))

        timer.wait_until("10min 10sec")

        updating_animation(p_pos_not_d_FPR[-1],self, color=GREEN_E)


        timer.wait_until("10min 12sec")
        
        ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)