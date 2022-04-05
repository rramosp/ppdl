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


def updating_animation(mobject,scene):
    scene.play(Circumscribe(mobject,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(mobject,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(mobject,color=BLUE_B,time_width=3))


class Main(Scene):
    def construct(self):

        video_name = r"bayes theorem intuition part 02"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-01-intuition-part-02-ES")
        self.add_sound(sfile)

        bayes_definition_tex = MathTex(
            "P", "(", "A", "|", "B", ")", "=", "{P(B|A)", "P(A)", "\\over", "P(B)} ", color=BLACK)

        bayes_with_sun_and_rain = MathTex(
            "P(sun|rain)", "=", "{P(rain|sun)", "\cdot", "P(sun)", "\\over", "P(rain)}", color=BLACK).next_to(bayes_definition_tex, DOWN*1.3)

        p_sun_rain_with_add_tex = MathTex( "P(sun|rain)", "=","{P(rain+sun)","\\over","P(rain)}", color=BLACK)

        p_rain_plus_sun = MathTex("P(rain+sun)", "=","P(sun|rain)","\cdot","P(rain)",color=BLACK).next_to(p_sun_rain_with_add_tex,DOWN)


        self.play(FadeIn(bayes_definition_tex))

        timer.wait_until(24)
        

        self.play(FadeIn(bayes_with_sun_and_rain))

        timer.wait_until(30)
        
        self.play(ReplacementTransform(bayes_with_sun_and_rain,bayes_definition_tex))

        
        timer.wait_until(45)

        bayes_with_sun_and_rain = MathTex(
            "P(sun|rain)", "=", "{P(rain|sun)", "\cdot", "P(sun)", "\\over", "P(rain)}", color=BLACK)

        self.play(FadeOut(bayes_definition_tex))
        self.play(FadeIn(bayes_with_sun_and_rain))
        

        timer.wait_until(51)

        self.play(bayes_with_sun_and_rain.animate.to_edge(UP).scale(0.8))
        self.play(Write(SurroundingRectangle(bayes_with_sun_and_rain,color=BLACK,stroke_width=0.2)))
        self.play(Write(p_sun_rain_with_add_tex,run_time=14))

        timer.wait_until("1min 12sec")

        self.play(Indicate( Group(p_sun_rain_with_add_tex[-3],p_sun_rain_with_add_tex[-1]),run_time=4,color=RED_E ) )
        self.play(Indicate(p_sun_rain_with_add_tex[0], color=RED_E, run_time=3))

        #p_sun_rain_with_add_tex = MathTex( "P(sun|rain)", "=","{P(rain+sun)\\overP(rain)}", color=BLACK)

        right_side_surround_indicate = SurroundingRectangle(p_sun_rain_with_add_tex[2:], buff=0.1,color=BLUE_E)
        no_observation_tex = Tex("No Observation", color=BLACK).next_to(p_sun_rain_with_add_tex[-1],DOWN)
        no_observation_tex.scale(0.5)

        self.play(FadeIn(right_side_surround_indicate))
        timer.wait_until("1min 23sec")
        self.play(Write(no_observation_tex))

        timer.wait_until("1min 29sec")

        left_side_underline = Underline(p_sun_rain_with_add_tex[0],color = RED_E)
        observation_tex = Tex("Observation", color= BLACK).next_to(p_sun_rain_with_add_tex[0],DOWN)
        observation_tex.scale(0.5)
        self.play(Write(left_side_underline))
        self.play(Write(observation_tex))
        timer.wait_until("1min 36sec")

        gained_info_tex = Tex("GAINED ", "INFORMATION",color=BLACK).next_to(p_sun_rain_with_add_tex[1],DOWN)
        gained_info_tex.scale(1.4)
        gained_info_tex.shift(DOWN*2)

        self.play(Write(gained_info_tex))
        
        updating_animation(gained_info_tex,self)

        timer.wait_until("1min 57sec")
        self.play(FadeOut(Group(observation_tex,no_observation_tex,right_side_surround_indicate,left_side_underline,gained_info_tex)))
        
        self.play(Write(p_rain_plus_sun,run_time=6))
        
        timer.wait_until("2min 4sec")
        self.play(Indicate(p_sun_rain_with_add_tex[-1],color=RED_E,run_time=4))

        timer.wait_until("2min 18sec")

        right_side_indicate_01 = Underline(p_rain_plus_sun[2],color=RED_E)
        right_side_indicate_02 = Underline(p_rain_plus_sun[-1],color=RED_E)

        self.play(Write(VGroup(right_side_indicate_01,right_side_indicate_02),run_time=3))

        timer.wait_until("2min 23sec")

        left_side_indicate = Underline(p_rain_plus_sun[0],color=RED_E)

        self.play(Write(left_side_indicate,run_time=2))

        timer.wait_until("2min 31sec")
        
        observation_tex.next_to(p_rain_plus_sun[2],DOWN)
        observation_tex.scale(1)

        self.play(Write(observation_tex,run_time=2))

        no_observation_tex.next_to(p_rain_plus_sun[-1],DOWN)
        no_observation_tex.scale(1)
        self.play(Write(no_observation_tex,run_time=2))

        timer.wait_until("2min 42sec")

        no_observation_tex_left_side = no_observation_tex.copy()
        no_observation_tex_left_side.next_to(p_rain_plus_sun[0],DOWN)
        no_observation_tex_left_side.scale(1)
        self.play(Write(no_observation_tex_left_side,run_time=2))

        timer.wait_until("2min 48sec")

        probabilities_vgroup = VGroup(Tex("P(rain)",color=BLACK),Tex("P(sun+rain)",color=BLACK), Tex("P(sun)",color=BLACK))
        probabilities_vgroup.arrange(direction=DOWN)
        surrounder_probabilities = SurroundingRectangle(probabilities_vgroup,color=BLACK,buff=0.3,stroke_width=0.2)
        header_probabilities_tex = Tex("non-conditional probabilities",color=BLACK).next_to(surrounder_probabilities,UP,buff=SMALL_BUFF)
        wrapper_probabilities_vgroup = VGroup(probabilities_vgroup,surrounder_probabilities,header_probabilities_tex).scale(0.7).to_edge(LEFT,MED_SMALL_BUFF)

        self.play(Write(probabilities_vgroup,run_time=6))
        self.play(Create(surrounder_probabilities))
        self.play(Write(header_probabilities_tex),run_time=3)

        timer.wait_until("3min 1sec")

        updating_animation(bayes_with_sun_and_rain[0],self)

        timer.wait_until("3min 8sec")
        self.play(Indicate(p_rain_plus_sun,color=RED_E,run_time=4))

        timer.wait_until("3min 15sec")
        self.play(Indicate(p_rain_plus_sun[2], color=GREEN_E, run_time=5))

        timer.wait_until("3min 21sec")
        self.play(Indicate(p_rain_plus_sun[2], color=RED_E, run_time=3))

        timer.wait_until("3min 25sec")
        self.play(Indicate(p_rain_plus_sun[0], color=BLUE_E, run_time=6))

        timer.wait_until("3min 36sec")
        vgroup_equations = VGroup(p_sun_rain_with_add_tex,p_rain_plus_sun,no_observation_tex,observation_tex,right_side_indicate_01,right_side_indicate_02,left_side_indicate,no_observation_tex_left_side)

        self.play(vgroup_equations.animate.shift(UP*2).scale(0.8))
        p_sun_vertline_rain = p_rain_plus_sun.copy()
        self.add(p_sun_vertline_rain)
        self.play(p_sun_vertline_rain.animate.to_edge(DOWN,LARGE_BUFF))

        timer.wait_until("3min 40sec")
        integrate_generalize_label = Text("INTEGRATE",stroke_width=1,color = BLACK).next_to(p_sun_vertline_rain,UP,buff=MED_SMALL_BUFF)
        generalize_text = Text("GENERALIZE",stroke_width=1,color = BLACK).next_to(p_sun_vertline_rain,DOWN,buff=MED_SMALL_BUFF)
        vgroup_label_p_sun_vertline_rain = VGroup(p_sun_vertline_rain,integrate_generalize_label, generalize_text)   
        surrounder_p_sun_vertline_rain = SurroundingRectangle(vgroup_label_p_sun_vertline_rain, color = BLACK, buff = MED_LARGE_BUFF) 
        vgroup_wrapper_p_sun_vertline_rain = VGroup(surrounder_p_sun_vertline_rain,vgroup_label_p_sun_vertline_rain)

        self.play(Write(integrate_generalize_label, run_time=2))
        self.play(FadeIn(surrounder_p_sun_vertline_rain))

        

        timer.wait_until("3min 45sec")
        self.play(Write(generalize_text, run_time=3))
        self.play(Indicate(generalize_text,color=RED_E,run_time=2))
        self.play(ReplacementTransform(generalize_text,integrate_generalize_label))
        


        timer.wait_until("4min 9sec")
        
        info_gain_vgroup = VGroup(Tex("- more observations",color=BLACK),Tex("- bigger dataset",color=BLACK),Tex("- data insights",color=BLACK),Tex("- parameter optimization",color=BLACK)).scale(1)
        info_gain_vgroup.arrange(direction=DOWN,buff=0.5)
        surrounder_info_gain = SurroundingRectangle(info_gain_vgroup,buff=0.3,color=BLACK,stroke_width=0.2)
        header_info_gain_tex = Tex("when do I gain information?",color=BLACK).next_to(surrounder_info_gain,UP)
        
        wrap_info_gain_vgroup = VGroup(header_info_gain_tex,surrounder_info_gain,info_gain_vgroup).scale(0.7).to_edge(RIGHT,buff=MED_SMALL_BUFF)

        self.play(FadeIn(wrap_info_gain_vgroup))

        timer.wait_until("4min 50sec")

        p_hyperparameters_to_data = MathTex("P(\\theta|data)",color=BLACK).next_to(p_rain_plus_sun,DOWN*3.5)
        self.play(Write(p_hyperparameters_to_data,run_time=4))

        timer.wait_until("4min 56sec")
        p_data_to_hyperparameters = MathTex("P(data|\\theta)",color=BLACK).next_to(p_hyperparameters_to_data,DOWN)
        self.play(Write(p_data_to_hyperparameters,run_time=8))


        timer.wait_until("6min 11sec")

        self.wait(5)
        play_credits(self)

        self.wait(5)