from manim import *


class Main(Scene):
    def construct(self):

        self.camera.background_color = WHITE

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

        self.play(GrowFromCenter(circles_vdict, run_time=3))
        self.play(circles_vdict.animate.scale(0.4).to_edge(LEFT))
        self.wait(2)
        self.play(Write(p_rain_text.scale(
            0.6).to_corner(UR, buff=0.5).shift(LEFT*3)))
        self.wait(2)

        self.play(Write(p_sun_text.scale(0.6).next_to(
            p_rain_text, RIGHT).shift(RIGHT)))
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

        self.wait(4)
        self.play(circles_vdict.animate.scale(1.2).shift(RIGHT*1.5))
        surrounder_circles = SurroundingRectangle(
            circles_vdict, color=GRAY, buff=LARGE_BUFF)

        self.play(Write(surrounder_circles))

        self.wait(4)
        self.play(FadeIn(fog_group))

        self.wait(2)
        self.play(FadeOut(fog_group))
        hail_group.next_to(rain_circle, DOWN, buff=-0.5)

        self.play(FadeIn(hail_group))

        self.wait(4)
        self.play(FadeOut(hail_group))

        self.wait(3)
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
        self.wait(2)
        self.play(Write(p_sun_if_rain.scale(0.6).move_to(
            p_rain_sun_text, DOWN).shift(DOWN*1.6).shift(LEFT*2)))

        self.wait(2)
        self.play(Write(expression_value_tex.scale(0.6).move_to(
            p_sun_if_rain, RIGHT).shift(UP*0.6).shift(RIGHT*2)),run_time=3)
        self.play(Write(expression_meaning_tex.scale(0.6).move_to(
            p_sun_if_rain, RIGHT).shift(DOWN*0.5).shift(RIGHT*2.3)),run_time=2)

        value_arrow = Arrow(p_sun_if_rain, expression_value_tex,
                            color=BLACK, buff=0.2).scale(0.6)
        meaning_arrow = Arrow(
            p_sun_if_rain, expression_meaning_tex, color=BLACK, buff=0.2).scale(0.6)
        arrow_vgroup = VGroup(value_arrow, meaning_arrow)
        self.play(Write(arrow_vgroup))

        self.wait(2)
        self.play(Indicate(p_sun_if_rain), color=RED_E, run_time=4)

        self.wait(1)
        formula_highlight_1 = SurroundingRectangle(
            p_sun_if_rain[-2], buff=.02, color=BLUE_E, stroke_width=DEFAULT_STROKE_WIDTH/3)
        self.play(Indicate(p_sun_if_rain[-2], color=BLUE_E))
        self.play(Create(Underline(p_sun_if_rain[-2], color=BLUE_E)))

        self.wait(2)
        p_rain_full_tex = MathTex(
            "P(", "rain", ")", "=", "1.0", color=BLUE_E, stroke_width=2)
        self.play(Write(p_rain_full_tex.scale(0.6).move_to(
            p_sun_if_rain, DOWN).shift(DOWN*0.6).shift(LEFT*0.1)),run_time=7)
        self.play(
            Create(Arrow(p_sun_if_rain[-2], p_rain_full_tex, color=BLUE_E).scale(0.3)))

        self.wait(2)
        self.play(Write(p_sun_if_rain_longer.scale(0.6).move_to(
            p_sun_if_rain, DOWN).shift(DOWN*2).shift(RIGHT*0.5)),run_time=16)
        self.wait(1)
        self.play(Write(p_sun_if_rain_longer_numeric.scale(
            0.6).next_to(p_sun_if_rain_longer, RIGHT)),run_time=12)

        self.wait(1)
        self.play(Write(p_rain_if_sun_longer.scale(
            0.6).next_to(p_sun_if_rain_longer, DOWN)),run_time=15)
        self.wait(1)
        self.play(Write(p_rain_if_sun_longer_numeric.scale(
            0.6).next_to(p_rain_if_sun_longer, RIGHT)),run_time=8)

        p_rain_plus_sun_Indicate_list = Group(
            p_sun_if_rain_longer[2], p_rain_if_sun_longer[2])
        p_sun_if_rain_Indicate_list = Group(
            p_sun_if_rain_longer[0], p_rain_if_sun_longer[0])
        self.wait(2)
        self.play(Indicate(p_rain_plus_sun_Indicate_list),
                  color=RED_E, run_time=7)
        self.wait(1)
        self.play(Indicate(p_sun_if_rain_Indicate_list),
                  color=RED_E, run_time=6)

        self.wait(2)
        self.play(Write(p_rain_plus_sun_longer.scale(0.6).next_to(p_rain_if_sun_longer,DOWN)),run_time=20)

        self.wait(5)
        prob_sun_if_rain_underline = Underline(p_rain_plus_sun_longer[2],color=BLUE_E)
        prob_rain_if_sun_underline = Underline(p_rain_plus_sun_longer[6],color=BLUE_E)
        prob_underlines_group = Group(prob_sun_if_rain_underline,prob_rain_if_sun_underline)
    
        self.play(Create(prob_sun_if_rain_underline))
        self.wait(1)
        self.play(Create(prob_rain_if_sun_underline))
        self.wait(2)
        self.play(FadeOut(prob_rain_if_sun_underline))

        self.wait(2)
        self.play(Write(bayes_with_sun_and_rain.scale(0.6).next_to(p_rain_plus_sun_longer,DOWN).shift(DOWN*0.2)),run_time=11)

        self.wait(4)
        self.play(FadeIn(rain_sun_to_definition.scale(0.6).next_to(bayes_with_sun_and_rain,LEFT).shift(LEFT*0.3)),run_time=3)
        self.play(Write(bayes_definition_tex.scale(0.6).next_to(rain_sun_to_definition,LEFT).shift(LEFT*0.3)),run_time=11)

        self.wait(2)
       
        

        self.wait(8)
