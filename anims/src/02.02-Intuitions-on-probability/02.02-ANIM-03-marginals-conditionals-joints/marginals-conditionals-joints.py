from __future__ import division
from lib2to3.pgen2.token import RIGHTSHIFT
import sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *

sys.path.insert(0, ".")

config.max_files_cached = 1000


class Main(Scene):
    def construct(self):

        video_name = r"marginals and conditionals joints"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("basics-02-marginals-conditionals-joints")
        
        self.add_sound(sfile)

        timer.wait_until(4)
        
        party_votes_img = get_imgmobject("party-votes-dataframe")

        self.play(
            FadeIn(party_votes_img)
        )

        timer.wait_until(8)

        party_rectangle = Rectangle(
                        color=RED_E,
                        height=party_votes_img.height,
                        width=party_votes_img.width/4
                        ).align_to(party_votes_img,UP).align_to(party_votes_img,LEFT)

        city_rectangle = Rectangle(
                        color=BLUE_E,
                        height=party_votes_img.height/5,
                        width=party_votes_img.width
                        ).align_to(party_votes_img,UP).align_to(party_votes_img,LEFT)



        self.play(
            Create(party_rectangle)
        )
        self.play(
            Uncreate(party_rectangle)
        )

        self.play(
            Create(city_rectangle)
        )
        self.play(
            Uncreate(city_rectangle)
        )

        timer.wait_until(27)

        self.play(
            party_votes_img.animate.to_edge(LEFT,buff=MED_SMALL_BUFF)
        )

        timer.wait_until(29)

        people_tex = MathTex("People").scale(1).next_to(party_votes_img,RIGHT).shift(RIGHT)

        self.play(
            Write(
                people_tex
            )
        )

        timer.wait_until(35)

        discrete_tex = MathTex("\\rightarrow ", "discrete").scale(1).next_to(people_tex)


        self.play(
            Write(discrete_tex[-1])
        )

        self.play(
            Write(discrete_tex[0])
        )

        timer.wait_until(37)
        
        people_vgroup = VGroup(people_tex,discrete_tex)

        self.play(
            people_vgroup.animate.shift(UP)
        )

        party_tex = MathTex("Party").scale(0.7).next_to(discrete_tex[0],DOWN).shift(DOWN*0.5)
        city_tex = MathTex("City").scale(0.7).next_to(party_tex, DOWN)

        self.play(
            Write(party_tex)
        )
        
        timer.wait_until(40)

        self.play(
            Write(city_tex)
        )

        timer.wait_until(51)

        four_rectangle = Rectangle(
                        color=RED_E,
                        height=party_votes_img.height/5,
                        width=party_votes_img.width/4
                        ).align_to(party_votes_img,UP).align_to(party_votes_img,RIGHT).shift(DOWN*0.8)

        self.play(
            Create(four_rectangle)
        )
        self.play(
            Uncreate(four_rectangle)
        )

        timer.wait_until("1min 5sec")

        self.play(
            FadeOut(party_tex),
            FadeOut(city_tex)
        )

        percentage_votes_x_tex = Text(
            "- % of votes for party_x?"
        ).scale(0.6).next_to(party_tex, RIGHT).shift(RIGHT*1.8).shift(UP*0.5)

        percentage_votes_city_y_tex = Text(
            "- % of votes on city_y?"
        ).scale(0.6).next_to(percentage_votes_x_tex,DOWN)

        diff_votes_winner_party_tex = Text(
            "-  % of advantage from the winning party?"
        ).scale(0.6).next_to(percentage_votes_city_y_tex,DOWN)

        votes_per_city = Text(
            "- which party won on city_z? By how many % points? "
        ).scale(0.6).next_to(diff_votes_winner_party_tex,DOWN)

        vgroup_bulletpoints = VGroup(percentage_votes_x_tex, percentage_votes_city_y_tex, diff_votes_winner_party_tex, votes_per_city)

        self.play(
            Write(
                percentage_votes_x_tex
            )
        )

        timer.wait_until("1min 14sec")

        self.play(
            Write(
                percentage_votes_city_y_tex
            )
        )

        timer.wait_until("1min 26sec")

        self.play(
            Write(
                diff_votes_winner_party_tex
            )
        )

        timer.wait_until("1min 38sec")

        self.play(
            Write(
                votes_per_city
            )
        )

        timer.wait_until("2min 15sec")

        
        updating_animation(party_votes_img,self,color=RED_E,time_width=6)
        

        timer.wait_until("2min 50sec")

        sum_votes_rectangle = Rectangle(
                                color=RED_E,
                                height= party_votes_img.height - party_votes_img.height/5,
                                width= party_votes_img.width - party_votes_img.width/4
                            ).align_to(party_votes_img,DOWN).align_to(party_votes_img,RIGHT)

        self.play(
            Create(sum_votes_rectangle)
        )

        sum_total_tex = MathTex(
            "324", color=RED_E
        ).next_to(sum_votes_rectangle,DOWN)

        timer.wait_until("2min 52sec")

        self.play(
            Write(sum_total_tex)
        )

        timer.wait_until("2min 55sec")

        self.play(
            FadeOut(sum_total_tex),
            Uncreate(sum_votes_rectangle)
        )

        timer.wait_until("2min 58sec")

        self.play(
            FadeOut(vgroup_bulletpoints),
            FadeOut(people_vgroup)
        )

        self.play(
            party_votes_img.animate.move_to(ORIGIN)
        )

        joint_prob_distr_img = get_imgmobject("joint-prob-distr-dataframe")

        self.play(
            ReplacementTransform(party_votes_img,joint_prob_distr_img)
        )

        updating_animation(joint_prob_distr_img, self, RED_E)

        timer.wait_until("3min 7sec")

        joint_sum_rectangle = Rectangle(
                                color=RED_E,
                                height= joint_prob_distr_img.height - joint_prob_distr_img.height/5,
                                width= joint_prob_distr_img.width - joint_prob_distr_img.width/4
                            ).align_to(joint_prob_distr_img,DOWN).align_to(joint_prob_distr_img,RIGHT)

        sum_one_tex = MathTex("1", color = RED_E).next_to(joint_sum_rectangle,DOWN)

        self.play(
            Create(joint_sum_rectangle)
        )
        
        timer.wait_until("3min 11sec")

        self.play(
            Write(sum_one_tex)
        )

        


        timer.wait_until("3min 20sec")


        self.play(
            FadeOut(sum_one_tex)
        )

        self.play(
            Uncreate(joint_sum_rectangle)
        )

        self.play(
            joint_prob_distr_img.animate.shift(UP*1.5)
        )

        xp_tex =  MathTex(
            "x_{p}", "=" , "random \hspace{0.2cm} variable \hspace{0.2cm} parties"
        ).scale(1).next_to(joint_prob_distr_img,DOWN).shift(DOWN*0.5)

        xc_tex = MathTex(
            "x_{c}", "=" , "random \hspace{0.2cm} variable \hspace{0.2cm} cities"
        ).scale(1).next_to(xp_tex,DOWN)

        

        timer.wait_until("3min 23sec")

        self.play(
            Write(xp_tex)
        )

        timer.wait_until("3min 30sec")

        self.play(
            Write(xc_tex)
        )

        random_var_vgroup = VGroup(xp_tex,xc_tex)

        timer.wait_until("3min 38sec")

        self.play(
            random_var_vgroup.animate.shift(LEFT*4)
        )

        timer.wait_until("3min 48sec")

        prob_example_tex = MathTex(
            "P(", "x_{p}", "=", "party_1", "," ,"x_{c}", "=", "city_3", ")" , "=" , "0.151"
        ).next_to(joint_prob_distr_img,DOWN).shift(RIGHT*4).shift(DOWN*0.5)

        self.play(
            Write(prob_example_tex[0:-2])
        )

        timer.wait_until("4min 10sec")

        prob_example_rectangle = Rectangle(
                        color=RED_E,
                        height=joint_prob_distr_img.height/5,
                        width=joint_prob_distr_img.width/4
                        ).align_to(joint_prob_distr_img,UP).align_to(joint_prob_distr_img,RIGHT).shift(DOWN*0.4)

        self.play(
            Create(prob_example_rectangle)
        )

        timer.wait_until("4min 14sec")

        self.play(
            Write(prob_example_tex[-2:])
        )

        timer.wait_until("4min 19sec")

        self.play(
            Uncreate(prob_example_rectangle)
        )

        timer.wait_until("4min 28sec")

        prob_unique_var_tex = MathTex(
            "P(", "x_{p}", "=" , "party_2", ")", "=", "0.376"
        ).next_to(prob_example_tex,DOWN)

        self.play(
            Write(
                prob_unique_var_tex[0:-2]
            )
        )

        timer.wait_until("4min 46sec")

        party_2_rectangle =  Rectangle(
                        color=RED_E,
                        height=joint_prob_distr_img.height/5,
                        width=joint_prob_distr_img.width
                        ).align_to(joint_prob_distr_img,UP).align_to(joint_prob_distr_img,LEFT).shift(DOWN*0.8)

        self.play(
            Create(party_2_rectangle)
        )

        timer.wait_until("4min 56sec")

        self.play(
            Write(prob_unique_var_tex[-2:])
        )

        timer.wait_until("5min 1sec")

        self.play(
            Uncreate(party_2_rectangle)
        )

        timer.wait_until("5min 17sec")

        city_3_rectangle = Rectangle(
                        color=BLUE_E,
                        height=joint_prob_distr_img.height,
                        width=joint_prob_distr_img.width/4
                        ).align_to(joint_prob_distr_img,UP).align_to(joint_prob_distr_img,RIGHT)

        self.play(
            Create(city_3_rectangle)
        )

        timer.wait_until("5min 25sec")

        p_city_3_tex = MathTex(
            "P(", "x_{c}=c_{3})", "=" , "0.268"
        ).next_to(prob_unique_var_tex,DOWN)

        self.play(
            Write(p_city_3_tex[0:-2])
        )

        timer.wait_until("5min 32sec")

        self.play(
            Write(p_city_3_tex[-2:])
        )

        timer.wait_until("5min 37sec")

        self.play(
            Uncreate(city_3_rectangle)
        )

        timer.wait_until("5min 49sec")

        probs_vgroup = VGroup(prob_example_tex,p_city_3_tex,prob_unique_var_tex)

        self.play(
            random_var_vgroup.animate.scale(0.7).next_to(joint_prob_distr_img,LEFT).shift(LEFT*0.5),
            probs_vgroup.animate.shift(LEFT*4)
        )

        timer.wait_until("5min 51sec")

        p_party_1_tex = MathTex(
            "P(", "x_{p}", "=","party_1", ")",
            "=",
            "\sum_{i}", "P(", "x_{p}= party_1", "|", "x_{c}=c_{i}", ")"
        ).next_to(p_city_3_tex,DOWN)

        self.play(
            Write(p_party_1_tex[0:5])
        )

        timer.wait_until("6min")

        self.play(
            Write(p_party_1_tex[6:])
        )

        self.play(
            Write(p_party_1_tex[5])
        )

        timer.wait_until("6min 25sec")

        self.play(
            Indicate(
                p_party_1_tex[1:4],
                color=RED_E,
                run_time=2
            )
        )

        timer.wait_until("7min 1sec")

        self.play(
            FadeOut(probs_vgroup),
            p_party_1_tex.animate.shift(UP*2)
        )

        p_party_2_tex = MathTex(
            "P(", "x_{p}", "=","party_2", ")"
        ).next_to(p_party_1_tex,DOWN)

        p_party_3_tex = MathTex(
            "P(", "x_{p}", "=","party_3", ")"
        ).next_to(p_party_2_tex,DOWN)

        p_party_4_tex = MathTex(
            "P(", "x_{p}", "=","party_4", ")"
        ).next_to(p_party_3_tex,DOWN)

        

        self.play(
            Write(p_party_2_tex),
            Write(p_party_3_tex),
            Write(p_party_4_tex),
        )

        timer.wait_until("7min 10sec")
        
        updating_animation(
            [p_party_1_tex[0:5], p_party_2_tex,p_party_3_tex,p_party_4_tex],
            self,
        )

        timer.wait_until("7min 19sec")

        marginals_sum_tex = MathTex(
            "\sum_{i} P(x_{p} = p_{i}) = 1"
        ).next_to(p_party_3_tex,RIGHT).shift(RIGHT)

        self.play(
            Write(marginals_sum_tex)
        )

        timer.wait_until("7min 36sec")

        marginal_p_xparties_tex = MathTex(
            "P(x_{p})"
        ).next_to(marginals_sum_tex,DOWN)

        self.play(
            Write(marginal_p_xparties_tex)
        )

        timer.wait_until("7min 46sec")

        marginal_p_xcities_tex = MathTex(
            "P(x_{c})"
        ).next_to(marginals_sum_tex,DOWN).shift(RIGHT)

        self.play(
            marginal_p_xparties_tex.animate.shift(LEFT)
        )

        self.play(FadeIn(marginal_p_xcities_tex))


        timer.wait_until("8min")

        self.play(
            FadeOut(
                *self.mobjects
            )
        )
  

        timer.wait_until("8min 9sec")

        self.play(
            FadeIn(
                joint_prob_distr_img
            )
        )

        question_1_text = Text(
            "- which party won on city_3?"
        ).next_to(joint_prob_distr_img,DOWN).shift(DOWN*0.5)

        question_2_text = Text(
            "- % of votes for the winner party"
        ).next_to(question_1_text,DOWN)

        self.play(
            Write(question_1_text)
        )

        timer.wait_until("8min 16sec")

        self.play(
            Write(question_2_text)
        )

        timer.wait_until("8min 29sec")

        city_3_rectangle = Rectangle(
                        color=BLUE_E,
                        height=joint_prob_distr_img.height,
                        width=joint_prob_distr_img.width/4
                        ).align_to(joint_prob_distr_img,UP).align_to(joint_prob_distr_img,RIGHT)

        self.play(
            Create(
                city_3_rectangle
            )
        )

        timer.wait_until("8min 41sec")

        city_3_diff_label = MathTex(
            "\\neq", "1", color=BLUE_E
        ).next_to(city_3_rectangle,DOWN)

        question_vgroup = VGroup(question_1_text,question_2_text)

        self.play(
            FadeIn(city_3_diff_label),
            question_vgroup.animate.shift(DOWN)
        )

        timer.wait_until("8min 57sec")

        prob_example_rectangle = Rectangle(
                        color=RED_E,
                        height=joint_prob_distr_img.height/5,
                        width=joint_prob_distr_img.width/4
                        ).align_to(joint_prob_distr_img,UP).align_to(joint_prob_distr_img,RIGHT).shift(DOWN*0.4)

        self.play(
            Create(prob_example_rectangle),
        )

        timer.wait_until("9min 26sec")

        self.play(
            Uncreate(prob_example_rectangle),
            Uncreate(city_3_rectangle),
            FadeOut(city_3_diff_label)
        )


        normalize_tex = MathTex(
            "NORMALIZE"
        ).next_to(joint_prob_distr_img,RIGHT).shift(RIGHT)

        self.play(Write(normalize_tex))

        updating_animation(normalize_tex,self)

        self.play(
            FadeOut(normalize_tex)
        )

        timer.wait_until("9min 37sec")

        self.play(
            FadeOut(question_1_text,question_2_text)
        )

        self.play(
            joint_prob_distr_img.animate.to_edge(UP)
        )

        normalize_equation_tex = MathTex(
            "P", "(", "x_{p} | x_{city_3} ", ")",
            "=",
            "{0.151", " \over ", "0.151+0.012+0.099+0.006}"
        ).next_to(joint_prob_distr_img,DOWN).shift(DOWN*0.5)

        self.play(
            Write(normalize_equation_tex[0:4])
        )

        timer.wait_until("9min 42sec")

        updating_animation(normalize_equation_tex[2], self, color=RED_E)

        timer.wait_until("9min 50sec")

        conditional_prob_tex = MathTex(
            "conditional \hspace{0.2cm} probability"
        ).next_to(normalize_equation_tex[0:4],DOWN)
        
        self.play(
            FadeIn(conditional_prob_tex)
        )

        updating_animation(conditional_prob_tex, self, RED_E)

        self.play(FadeOut(conditional_prob_tex))

        timer.wait_until("10min 5sec")

        prob_example_rectangle = Rectangle(
                        color=RED_E,
                        height=joint_prob_distr_img.height/5,
                        width=joint_prob_distr_img.width/4
                        ).align_to(joint_prob_distr_img,UP).align_to(joint_prob_distr_img,RIGHT).shift(DOWN*0.4)

        city_3_rectangle = Rectangle(
                        color=BLUE_E,
                        height=joint_prob_distr_img.height,
                        width=joint_prob_distr_img.width/4
                        ).align_to(joint_prob_distr_img,UP).align_to(joint_prob_distr_img,RIGHT)

        self.play(
            Create(prob_example_rectangle),
            Uncreate(prob_example_rectangle)
        )

        self.play(
            Create(city_3_rectangle),
            Uncreate(city_3_rectangle)
        )

        timer.wait_until("10min 11sec")

        self.play(
            Write(
                normalize_equation_tex[4:]
            )
        )

        timer.wait_until("10min 34sec")

        normalize_equation_1_tex = MathTex(
            "P", "(", "x_{p} = party_1 | x_{city_3} ", ")"
        ).next_to(normalize_equation_tex,DOWN).shift(DOWN*0.3)

        normalize_equation_2_tex = MathTex(
            "P", "(", "x_{p} = party_2 | x_{city_3} ", ")"
        ).next_to(normalize_equation_1_tex,DOWN)

        normalize_equation_3_tex = MathTex(
            "P", "(", "x_{p} = party_3 | x_{city_3} ", ")"
        ).next_to(normalize_equation_2_tex,DOWN)

        normalize_equation_4_tex = MathTex(
            "P", "(", "x_{p} = party_4 | x_{city_3} ", ")"
        ).next_to(normalize_equation_3_tex,DOWN)

        self.play(
            Write(normalize_equation_1_tex)
        )

        timer.wait_until("10min 43sec")

        self.play(
            Write(normalize_equation_2_tex)
        )

        timer.wait_until("10min 50sec")

        self.play(
            Write(normalize_equation_3_tex),
            Write(normalize_equation_4_tex)
        )

        timer.wait_until("10min 57sec")

        normalized_numbers_vgroup = VGroup(
            normalize_equation_1_tex, normalize_equation_2_tex, normalize_equation_3_tex, normalize_equation_4_tex
        )

        normalized_vgroup_surrounder = SurroundingRectangle(normalized_numbers_vgroup,color=RED_E)

        self.play(
            Create(normalized_vgroup_surrounder)
        )
        

        timer.wait_until("11min 6sec")

        one_tex = MathTex(
            "1", color=BLUE_E
        ).next_to(normalized_vgroup_surrounder,DOWN)

        self.play(
            Write(one_tex)
        )

        timer.wait_until("11min 7sec")

        updating_animation(normalize_equation_tex[-3],self, RED_E)


        timer.wait_until("11min 13sec")
        
        updating_animation(normalize_equation_tex[-1], self, BLUE_E)

        timer.wait_until("11min 33sec")

        self.play(
            normalized_numbers_vgroup.animate.shift(LEFT*3),
            FadeOut(one_tex),
            Uncreate(normalized_vgroup_surrounder)
        )

        joint_distr_tex = MathTex(
            "P(x_p,x_c) \\rightarrow joint \hspace{0.2cm} distribution"
        ).next_to(normalize_equation_tex,DOWN).shift(DOWN*0.3).shift(RIGHT*3)

        self.play(
            Write(joint_distr_tex)
        )

        timer.wait_until("11min 49sec")

        marginal_p_tex = MathTex(
            "P(x_p)", "\\rightarrow", "marginal"
        ).next_to(joint_distr_tex, DOWN)

        marginal_c_tex = MathTex(
            "P(x_c)", "\\rightarrow", "marginal"
        ).next_to(marginal_p_tex, DOWN)

        self.play(
            Write(marginal_p_tex[0]),
            Write(marginal_c_tex[0])
        )

        timer.wait_until("11min 57sec")

        self.play(
            Write(marginal_p_tex[-1])
        )

        self.play(
            Write(marginal_c_tex[-1])
        )
        

        self.play(
            Write(
                marginal_p_tex[-2],
            )
        )

        self.play(
            Write(marginal_c_tex[-2])
        )

        timer.wait_until("12min 22sec")

        normalized_conditional_prob = MathTex(
            "P(x_p|x_c = c3)", "\\rightarrow", "for \hspace{0.2cm} each \hspace{0.2cm} conditional \hspace{0.2cm} value"
        ).scale(0.8).next_to(marginal_c_tex,DOWN)

        self.play(
            Write(normalized_conditional_prob)
        )


        ## credits
        self.wait(5)
        #play_credits(self)

        self.wait(5)