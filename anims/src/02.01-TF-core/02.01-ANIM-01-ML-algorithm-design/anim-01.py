import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
from scipy import stats
import pandas as pd

def play_scatter(scene):

    ax = get_axes(xmin=2, xmax=7,
                  ymin=6, ymax=16, 
                  x_length=4, y_length=3,
                  x_splits=6, y_splits=6,
                  show_y_numbers = True,
                  xlabel="length", 
                  xlabel_kwargs={'font_size': 24},
                  ylabel="scales density", 
                  ylabel_kwargs={'font_size': 24},
                  additional_x_axis_config={'decimal_number_config' : {'color': '#222222','num_decimal_places': 1 }},
                  additional_y_axis_config={'decimal_number_config' : {'color': '#222222','num_decimal_places': 1 }}

                  ).move_to([+2,-1,0])
    plane = ax[0]
        
    d = pd.read_csv("/manim/data/trilotropicos.csv")

    dots = [Dot(plane.c2p(x,y), radius=0.05, fill_opacity=0.5, color=BLUE_E) \
            for x,y in zip (d.longitud, d.densidad_escamas)]

    dots = VGroup(*dots)

    scene.play(FadeIn(ax))
    scene.play(Create(dots))

    return ax, dots


def get_random_line(plane):
    t0 = np.random.random()*5+9
    t1 = (np.random.random()-0.5)*2    
    return t0, t1, plane.plot(lambda x: t0 + t1*x, color=BLACK)

def get_good_line(plane):
    t0, t1 = 12, -0.6
    return t0, t1, plane.plot(lambda x: t0 + t1*x, color=BLACK)

def get_bad_line(plane):
    t0, t1 = 8, .7
    return t0, t1, plane.plot(lambda x: t0 + t1*x, color=BLACK)

def play_prediction(scene, plane, t0, t1, x, run_time=1):

    f = lambda x: t0 + t1*x
    vline = DashedLine(start=plane.c2p(x,6), end=plane.c2p(x,f(x)), 
                       stroke_width=1.5, dash_length=0.05, color=BLACK)
    hline = DashedLine(start=plane.c2p(x,f(x)), end=plane.c2p(2,f(x)), 
                       stroke_width=1.5, dash_length=0.05, color=BLACK)

    scene.play(Create(vline), run_time = run_time/2)
    scene.play(Create(hline), run_time = run_time/2)
    return VGroup(vline, hline)


def get_random_pos(xrange, yrange):
    x = np.random.random()*(xrange[1]-xrange[0]) + xrange[0]
    y = np.random.random()*(yrange[1]-yrange[0]) + yrange[0]
    return x,y,0

class Main(Scene):
    def construct(self):

        video_name = r"how are machine learning algorithms designed"
        play_intro_scene(self,video_name)
        
        sfile = find_soundfile("02.01-anim-01-ES") 
        self.add_sound(sfile)

        timer = SceneTimer(self,debug_wait=False).reset()

        t = MathTex(r"\text{Designing machine learning algorithms").to_edge(UP)

        ss = SVGMobject(find_imgfile("scientist"), height=4).shift(LEFT*3)
        sm = SVGMobject(find_imgfile("machines"), height=4).next_to(ss, RIGHT*15)
        tm = MathTex(r"\text{Machines DO NOT learn!!!!", color=RED_E).next_to(ss, DOWN)
        step1 = MathTex(r"\text{1. Define model assumption}", font_size=30, color=BLUE_E).to_edge(LEFT).shift(UP*2)
        step2 = MathTex(r"\text{2. Define model parametrization}", font_size=30, color=BLUE_E).next_to(step1, DOWN).align_to(step1, LEFT)
        step3 = MathTex(r"\text{3. Define how to make predictions}", font_size=30, color=BLUE_E).next_to(step2, DOWN).align_to(step2, LEFT)
        step4 = MathTex(r"\text{4. Define error (loss) function}", font_size=30, color=BLUE_E).next_to(step3, DOWN).align_to(step3, LEFT)
        step5 = MathTex(r"\text{5. Optimize !!! }\rightarrow\text{ minimize loss}", font_size=30, color=BLUE_E).next_to(step4, DOWN).align_to(step4, LEFT)
        step5n = MathTex(r"\text{5. Derive gradient}", font_size=30, color=BLUE_E).next_to(step4, DOWN).align_to(step4, LEFT)
        step6n = MathTex(r"\text{6. Optimize !!! }\rightarrow\text{ minimize loss}", font_size=30, color=BLUE_E).next_to(step5n, DOWN).align_to(step5n, LEFT)

        self.play(Write(t))

        self.wait(2)
        self.play(Create(ss, stroke_width=5), run_time=2)

        timer.wait_until(24)
        self.play(Create(sm, stroke_width=2), run_time=2)
        self.wait(2)
        self.play(Write(tm))


        timer.wait_until(45)
        self.play(FadeOut(sm))
        self.play(FadeOut(tm))

        strings = ["Decision Trees", "Support Vector Machines", "Neural Networks", "Linear Regression", 
                   "Random Forests", "Nearest Neighbors", "Discriminant Analysis", "Generalized Linear Models"]

        for _ in range(3):
            for s in np.random.permutation(strings):
                t = MathTex(r"\text{"+s+"}", font_size=24).move_to(get_random_pos([1,3],[-1,+1]))
                self.play(FadeIn(t, run_size=0.3))
                self.wait(.1)
                self.play(FadeOut(t, run_size=0.1))

        self.play(FadeOut(ss))

        timer.wait_until("1min 40sec")
        ax, dots = play_scatter(self)

        plane = ax[0]
        
        timer.wait_until("1min 50sec")
        xy = MathTex(r"x^{(i)}=\text{length }  \hspace{0.5cm} y^{(i)}=\text{density}", font_size=25).next_to(plane, UP*5)
        self.play(Write(xy))

        timer.wait_until("2min 07sec")
        xy_pairs = MathTex(r"(x^{(i)}, y^{(i)}) \text{ with } i \in \{0,...,N-1\}", font_size=25).next_to(xy, DOWN)
        self.play(Write(xy_pairs))

        timer.wait_until("2min 43sec")
        supervised = MathTex(r"\text{supervised learning}", font_size=25).next_to(xy_pairs, DOWN)
        self.play(Write(supervised))

        timer.wait_until("3min 10sec")
        self.play(Write(step1))


        timer.wait_until("3min 15sec")
        linf = plane.plot(lambda x: 12.8 - 0.7*x, color=BLACK, stroke_width=5)
        self.play(Create(linf))

        timer.wait_until("3min 20sec")
        quadf = plane.plot(lambda x: 26.75 - 7.61*x + 0.76*x**2, color=RED)
        self.play(Create(quadf))

        timer.wait_until("3min 50sec")
        self.play(Uncreate(quadf))
        self.play(FadeOut(xy, xy_pairs, supervised, linf))

        timer.wait_until("4min 05sec")
        overfit = MathTex(r"\text{overfitting").next_to(ax, UP)
        underfit = MathTex(r"\text{underfitting").next_to(overfit, RIGHT)
        self.play(Write(overfit))
        self.play(Write(underfit))

        timer.wait_until("4min 30sec")
        self.play(FadeOut(overfit, underfit))


        timer.wait_until("4min 41sec")
        self.play(Write(step2))

        timer.wait_until("4min 51sec")
        t01 = MathTex(r"\theta_0\text{ intercept}   \hspace{0.5cm}  \theta_1\text{ slope }", font_size=30).next_to(plane, UP*5)
        self.play(Write(t01))


        
        timer.wait_until("5min 13sec")
        t0, t1, line = get_random_line(plane)
        t_text = MathTex(r"\theta_0="+f"{t0:.2f}"+r" \hspace{0.5cm}  \theta_1="+f"{t1:.2f}", font_size=20).next_to(plane, UP)
        self.play(Create(line), Write(t_text))

        for _ in range(10):
            t0, t1, newline = get_random_line(plane)
            new_t_text = MathTex(r"\theta_0="+f"{t0:.2f}"+r" \hspace{0.5cm}  \theta_1="+f"{t1:.2f}", font_size=20).next_to(plane, UP)
            self.play(FadeOut(t_text), FadeIn(new_t_text), Transform(line, newline))
            t_text = new_t_text
            self.wait(0.5)

        timer.wait_until("5min 54sec")
        
        t0, t1, new_line = get_bad_line(plane)
        new_t_text = MathTex(r"\theta_0="+f"{t0:.2f}"+r" \hspace{0.5cm}  \theta_0="+f"{t1:.2f}", font_size=20).next_to(plane, UP)
        self.play(Transform(line, new_line), Transform(t_text, new_t_text))

        timer.wait_until("6min 00sec")
        t0, t1, new_line = get_good_line(plane)
        new_t_text = MathTex(r"\theta_0="+f"{t0:.2f}"+r" \hspace{0.5cm}  \theta_1="+f"{t1:.2f}", font_size=20).next_to(plane, UP)
        self.play(Transform(line, new_line), Transform(t_text, new_t_text))

        timer.wait_until("6min 40sec")
        self.play(Write(step3))

        for _ in range(5):
            x = np.random.random()*5+2
            px = t0 + t1*x
            tx  = MathTex(r"x="+f"{x:.2f}", font_size=20).move_to(plane.get_center()+UP)
            tpx = MathTex(r"\hat{y}="+f"{px:.2f}", font_size=20).next_to(tx, RIGHT)
            self.play(FadeIn(tx), run_time=0.2)
            lines = play_prediction(self, plane, t0=t0, t1=t1, x=x, run_time=2)        
            self.play(FadeIn(tpx, run_time=.2))
            self.wait(0.2)
            self.play(FadeOut(lines, tx, tpx))

        self.play(FadeOut(t01, t_text))

        pred_eq = MathTex(r"\hat{y}^{(i)} = \theta_0 + \theta_1 x^{(i)}", font_size=20).next_to(plane, UP*5)

        error_eq = MathTex(r"\text{error}^{(i)} = (\hat{y}^{(i)} - y^{(i)})^2", font_size=20).next_to(pred_eq, DOWN)

        loss_eq  = MathTex(r"\text{loss}(",r"\theta_0,\theta_1",r") = \frac{1}{N}\sum_{i=0}^{N-1}(\hat{y}^{(i)} - y^{(i)})^2", font_size=20)\
                   .next_to(error_eq, DOWN)

        argmin_eq = MathTex("\\"+r"underset{\theta_0 \theta_1}{\text{argmin}} \text{ loss}(\theta_0, \theta_1)", font_size=20)\
                    .next_to(error_eq, DOWN*2)


        timer.wait_until("7min 00sec")
        self.play(Write(pred_eq))

        timer.wait_until("7min 44sec")
        self.play(Write(step4))

        timer.wait_until("7min 58sec")
        self.play(Write(error_eq))


        timer.wait_until("8min 17sec")
        self.play(Write(loss_eq))

        timer.wait_until("8min 50sec")
        self.play(Indicate(loss_eq[1], scale_factor=2, color=BLACK))

        timer.wait_until("8min 57sec")
        self.play(FadeOut(error_eq))
        self.play(loss_eq.animate.shift(UP*0.5))

        timer.wait_until("9min 45sec")
        self.play(Write(argmin_eq))

        timer.wait_until("10min 05sec")
        self.play(Write(step5))


        partial_eq = MathTex(r"\nabla = \Big[\frac{\partial\text{loss}}{\partial \theta_0} \text{ } \frac{\partial\text{loss}}{\partial \theta_1}\Big] = \text{ the gradient}", font_size=25).to_edge(LEFT).shift(DOWN*2)
        diff_t0 = MathTex(r"\frac{\partial\text{loss}}{\partial\theta_0} = \frac{1}{N}\sum 2(\theta_0 + \theta_1 - y^{(i)})", font_size=20).next_to(partial_eq, DOWN).align_to(partial_eq, LEFT)
        diff_t1 = MathTex(r"\frac{\partial\text{loss}}{\partial\theta_1} = \frac{1}{N}\sum 2x^{(i)}(\theta_0 + \theta_1 x^{(i)} - y^{(i)})", font_size=20).next_to(diff_t0, DOWN).align_to(diff_t0, LEFT)

        timer.wait_until("10min 50sec")
        self.play(Write(partial_eq))

        timer.wait_until("11min 14sec")
        self.play(Write(diff_t0))
        self.play(Write(diff_t1))

        timer.wait_until("11min 41sec")
        self.play(Transform(step5, step6n))
        self.play(Write(step5n))

        timer.wait_until("11min 50sec")
        self.play(FadeOut(diff_t0, diff_t1, pred_eq, loss_eq, argmin_eq))
        self.play(FadeOut(ax, line, dots))

        self.wait(2)

        ss = ss.shift(RIGHT*3)
        ssmile = SVGMobject(find_imgfile("smile"), height=0.5).scale(1.22).next_to(ss, UP).shift(DOWN*1.4+RIGHT*0.08)


        tr1 = MathTex(r"\text{choose model structure}").next_to(ss, RIGHT*3).shift(UP)
        tr2 = MathTex(r"\text{choose loss function}").next_to(tr1, DOWN)
        tr3 = MathTex(r"\text{choose data}").next_to(tr2, DOWN)
        tr4 = MathTex(r"\text{obtain gradients}").next_to(tr3, DOWN)
        tr5 = MathTex(r"\text{use optimization algorithms}").next_to(tr4, DOWN)
        tr6 = MathTex(r"\text{use computing frameworks}").next_to(tr5, DOWN)
        trset = [tr1, tr2, tr3, tr4, tr5, tr6]

        cg1 = MathTex(r"\text{complexity of prediction function}", font_size=25).move_to([2,2,0])
        cg2 = MathTex(r"\text{complexity of loss function}", font_size=25).next_to(cg1, DOWN).align_to(cg1, LEFT)
        cg3 = MathTex(r"\text{number of descriptors}", font_size=25).next_to(cg2, DOWN).align_to(cg2, LEFT)
        cg4 = MathTex(r"\text{number of model parameters}", font_size=25).next_to(cg3, DOWN).align_to(cg3, LEFT)

        cg5 = MathTex(r"\text{RGB image: 200x200x3 descriptors", font_size=25).next_to(cg4, DOWN*3).align_to(cg4, LEFT)
        cg6 = MathTex(r"\text{AlexNet: 61M parameters", font_size=25).next_to(cg5, DOWN).align_to(cg5, LEFT)

        imgstack = get_imgmobject("imagestack").scale(0.8).next_to(cg4, DOWN*1.5)
        logosympy = get_imgmobject("sympy").scale(0.8).next_to(cg4, DOWN*1.5).shift(LEFT)
        logoscipy = get_imgmobject("scipy").scale(0.5).next_to(logosympy, RIGHT)

        logotf = get_imgmobject("logo-tf").scale(0.25).next_to(cg4, DOWN*1.5)
        logotorch= get_imgmobject("logo-pytorch").next_to(logotf, DOWN)

        lrgrad = MathTex(r"\nabla \text{loss} = \frac{1}{n}2X^{T}\cdot(X\cdot\theta-Y)").next_to(cg4, DOWN*2)
        lrX = MathTex(r"X \in \mathbb{R}^{n\times m}").next_to(lrgrad, DOWN).align_to(lrgrad, LEFT)
        lry = MathTex(r"Y \in \mathbb{R}^{n}").next_to(lrX, DOWN).align_to(lrX, LEFT)
        lrt = MathTex(r"\theta \in \mathbb{R}^{m}").next_to(lry, DOWN).align_to(lry, LEFT)
        lrg = MathTex(r"\nabla \in \mathbb{R}^{m}").next_to(lrt, DOWN).align_to(lrt, LEFT)


        mx0 = MathTex(r"---- x^{(0)} ----", font_size=20).next_to(cg4, DOWN*2)
        mx1 = MathTex(r"---- x^{(1)} ----", font_size=20).next_to(mx0, DOWN)
        mxi = MathTex(r"---- x^{(i)} ----", font_size=20).next_to(mx1, DOWN*2)
        mxn = MathTex(r"--- x^{(N-1)} ---", font_size=20).next_to(mxi, DOWN*2)

        bl = MathTex("[", font_size=200).next_to(mx1, LEFT).shift(DOWN*.5)
        br = MathTex("]", font_size=200).next_to(mx1, RIGHT).shift(DOWN*.5)

        x = MathTex("X =").next_to(bl, LEFT)
        rnm = MathTex(r"\in \mathbb{R}^{n\times m").next_to(br, RIGHT)

        isympy = MathTex(r"\texttt{import sympy}", font_size=20).next_to(logosympy, DOWN)
        iscipy = MathTex(r"\texttt{from scipy import optimize}", font_size=20).next_to(isympy, RIGHT)

        


        timer.wait_until("12min 03sec")
        self.play(Write(cg1))
        timer.wait_until("12min 11sec")
        self.play(Write(cg2))
        timer.wait_until("12min 16sec")
        self.play(Write(cg3))
        timer.wait_until("12min 20sec")
        self.play(Write(cg4))
        timer.wait_until("12min 32sec")
        self.play(Write(cg5))
        timer.wait_until("12min 47sec")
        self.play(Write(cg6))

        timer.wait_until("13min 10sec")
        self.play(FadeOut(cg5, cg6))

        timer.wait_until("13min 20sec")
        self.play(FadeIn(bl, br), *[Write(i) for i in [mx0, mx1, mxi, mxn, x, rnm]])


        timer.wait_until("13min 53sec")
        self.play(FadeOut(mx0, mx1, mxi, mxn, x, rnm, bl, br))

        self.play(FadeIn(imgstack))

        timer.wait_until("14min 18sec")
        self.play(FadeOut(imgstack))
        self.play(Write(lrgrad))


        timer.wait_until("14min 35sec")
        self.play(Write(lrX), Write(lry), Write(lrt), Write(lrg))
        
        timer.wait_until("15min 07sec")
        self.play(FadeOut(lrgrad, lrX, lry, lrt, lrg))

        timer.wait_until("15min 20sec")
        self.play(FadeIn(logosympy, logoscipy))
        self.play(Write(isympy), Write(iscipy))

        timer.wait_until("16min 20sec")
        self.play(FadeOut(logosympy, logoscipy, isympy, iscipy))

        timer.wait_until("16min 25sec")
        self.play(FadeIn(logotf, logotorch))

        timer.wait_until("17min 47sec")
        self.play(FadeOut(logotf, logotorch, cg1, cg2, cg3, cg4))

        self.play(FadeIn(ss))


        timer.wait_until("18min 02sec")
        self.play(Write(tr1))

        timer.wait_until("18min 12sec")
        self.play(Write(tr2))

        timer.wait_until("18min 15sec")
        self.play(Write(tr3))

        timer.wait_until("18min 20sec")
        self.play(Write(tr4))

        timer.wait_until("18min 24sec")
        self.play(Write(tr5))

        timer.wait_until("18min 28sec")
        self.play(Write(tr6))

        timer.wait_until("18min 50sec")
        self.play(FadeIn(ssmile))

        timer.wait_until("19min 03sec")
        for i in [step1, step2, step3, step4, step5n, step6n]:
            self.play(Indicate(i), color=BLACK)
            self.wait(0.5)

        timer.wait_until("19min 17sec")
        mdont = MathTex(r"\text{Machines DON'T learn. We use them to calibrate models.", font_size=50, color=RED_E).to_edge(DOWN)
        self.play(Write(mdont))
        timer.wait_until("19min 30sec")

        play_credits(self)
        self.wait(5)

