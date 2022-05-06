from manim import *
import numpy as np

class Main(Scene):

    def construct(self):
        
        h_tex = Tex("h = ").scale(1.4)
        h = Matrix([ [0.3],[0.4] , ["\\dots"], [0.6], [0.8] ]).next_to(h_tex,RIGHT)
        greater_than_tex = Tex("$\\geq$").next_to(h,RIGHT,buff=MED_LARGE_BUFF).scale(1.4)
    
        comparative_number = DecimalNumber(0.5).next_to(greater_than_tex,RIGHT,buff=MED_LARGE_BUFF).scale(1.4)
        comparation_vgroup = VGroup(h_tex,h,greater_than_tex,comparative_number)

        self.play(FadeIn(comparation_vgroup))
        self.play(comparation_vgroup.animate.to_edge(LEFT))

        pred_tex = Tex("pred = ").scale(1.4)
        pred = Matrix( [ [0], [0] , ["\\dots"], [1], [1] ] ).next_to(pred_tex,RIGHT)

        pred_vgroup = VGroup(pred_tex,pred).to_edge(RIGHT)

        self.play(FadeIn(pred.get_brackets(), pred_tex))   

        self.play(Indicate(VGroup(h[0][0], greater_than_tex,comparative_number),color=RED_E,scale_factor=1.1),run_time=4)
        self.play(ReplacementTransform(h[0][0], pred[0][0]))

        self.play(Indicate(VGroup(h[0][1], greater_than_tex,comparative_number),color=RED_E,scale_factor=1.1),run_time=4)
        self.play(ReplacementTransform(h[0][1], pred[0][1]))

        self.play(Indicate(VGroup(h[0][2], greater_than_tex,comparative_number),color=YELLOW_E,scale_factor=1.1),run_time=4)
        self.play(ReplacementTransform(h[0][2], pred[0][2]))

        self.play(Indicate(VGroup(h[0][3], greater_than_tex,comparative_number),color=GREEN_E,scale_factor=1.1),run_time=4)
        self.play(ReplacementTransform(h[0][3], pred[0][3]))

        self.play(Indicate(VGroup(h[0][4], greater_than_tex,comparative_number),color=GREEN_E,scale_factor=1.1),run_time=4)
        self.play(ReplacementTransform(h[0][4], pred[0][4]))

        self.wait(4)
