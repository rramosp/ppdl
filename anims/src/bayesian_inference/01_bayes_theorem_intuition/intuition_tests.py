from manim import *

class Main(Scene):
    def construct(self):

        self.camera.background_color = WHITE

        rain_circle = Circle(radius=3, color=BLUE_E,fill_opacity= 0.4, stroke_width=4).move_to(LEFT)
        sun_circle = Circle(radius=3,color=YELLOW_E, fill_opacity=0.4, stroke_width=4).move_to(RIGHT*2.5)

        sun_label = MathTex("sun" ,color=BLACK).next_to(sun_circle.get_corner(UR),buff=0.1)
        rain_label = MathTex("rain",color=BLACK).next_to(rain_circle.get_corner(UL),buff=-1.5)

        pairs = [("Rain", rain_circle), ("Sun", sun_circle),("sun_label",sun_label), ("rain_label", rain_label)]

        circles_vdict = VDict(pairs,show_keys=False)

        p_rain_text = MathTex(
            "P(rain)=", "0.6"
        ,color=BLUE_E,stroke_width=2)

        p_sun_text = MathTex(
            "P(sun)= ", "0.4"
        ,color=YELLOW_E,stroke_width=2)

        p_rain_sun_text = MathTex(
            "P(rain + sun)=", "0.3"
        ,color=GREEN_E, stroke_width = 0.8)

               



        self.play(GrowFromCenter(circles_vdict,run_time=3))
        self.play(circles_vdict.animate.scale(0.4).to_edge(LEFT))
        self.wait(2)     
        self.play(Write(p_rain_text.scale(0.6).to_corner(UR,buff=0.5).shift(LEFT*3)))
        self.wait(2)

        self.play(Write(p_sun_text.scale(0.6).next_to(p_rain_text,RIGHT).shift(RIGHT)))
        self.wait(2)


        intersection_rain_sun = Intersection(rain_circle,sun_circle,color=GREEN_E,fill_opacity=0.4,stroke_width=3)
        fog_circle = Circle(radius=0.5, color=GRAY, fill_opacity=0.7,stroke_width=4).move_to(intersection_rain_sun).shift(DOWN*1.5)
        fog_label = MathTex("fog",color=BLACK).move_to(fog_circle.get_corner(DR)).scale(0.6)
        fog_group = Group(fog_circle,fog_label).scale(1.2).shift(RIGHT*1.5)
        hail_circle = Circle(radius=0.5, color = TEAL_B , fill_opacity=0.7, stroke_width=4)
        hail_label = MathTex("hail", color=BLACK).move_to(hail_circle.get_corner(DR)).scale(0.6)
        hail_group = Group(hail_circle,hail_label).scale(1.2)

        self.play(Write(p_rain_sun_text.scale(0.6).move_to(p_rain_text.get_corner(DR)).shift(RIGHT*0.7).shift(DOWN*0.4)))
        self.play(intersection_rain_sun.animate.scale(0.6).move_to(p_rain_sun_text).shift(DOWN))
        self.play(Indicate(intersection_rain_sun,color=GREEN_D))
        self.play(FadeOut(intersection_rain_sun))
        
        self.wait(4)
        self.play(circles_vdict.animate.scale(1.2).shift(RIGHT*1.5))
        surrounder_circles = SurroundingRectangle(circles_vdict,color=GRAY, buff=LARGE_BUFF)

        self.play(Write(surrounder_circles))

        self.wait(4)
        self.play(FadeIn(fog_group))

        self.wait(2)
        self.play(FadeOut(fog_group))
        hail_group.next_to(rain_circle,DOWN,buff=-0.7)

        self.play(FadeIn(hail_group))

        self.wait(4)
        self.play(FadeOut(hail_group))

        self.wait(3)
        self.play(FadeOut(surrounder_circles))
        self.play(circles_vdict.animate.scale(1).shift(LEFT*1.3))

        self.wait(2)