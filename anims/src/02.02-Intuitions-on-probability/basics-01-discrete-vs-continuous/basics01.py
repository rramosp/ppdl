import logging
import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
from scipy import stats


def play_professions(scene):
    t1 = Text("P(engineer)= 3%", font_size=32).move_to([-4,0,0])
    t2 = Text("P(teacher)  = 0.5%", font_size=32).move_to([-4,-.8,0]).align_to(t1, LEFT)
    t3 = Text("P(trainer)   = 2%", font_size=32).move_to([-4,-1.6,0]).align_to(t2, LEFT)
    t4 = Text("etc.", font_size=32).move_to([-4,-2.4,0]).align_to(t3, LEFT)

    g = VGroup(t1, t2, t3, t4)
    scene.play(Write(g, run_time=6))
    return g

def play_cities_histogram(scene, position, transform_from=None):

    c = pd.read_csv("src/02.02-Intuitions-on-probability/intro-probability/basics-01-discrete-vs-continuous/data/cities_colombia.csv")
    c['2022'] = c['2022']/c['2022'].sum()*100
    c = c.head(20)
    c = c.sort_values(by="name")

    labels = c['name'].values
    vals = c['2022'].values

    h = histogram(  vals, 
                    title=r"\% of population in major cities in Colombia",
                    labels=labels,
                    hlines = [5,10,15,20],
                    hlines_labels = ["5%", "10%", "15%", "20%"],
                    font_size=13,
                    height=2.5, stroke_width=1,
                    binwidth=0.3, 
                    bingap=0.1,
                    color=BLUE_E,
                    fill_opacity=0.5
                 ).move_to([-3,0,0]).move_to(position)

    if transform_from is not None:
        scene.play(Transform(transform_from, h), run_time=5)
    else:
        scene.play(Create(h), run_time=5)
    return h



def play_age_histogram(scene, position, transform_from=None):
        h = histogram(  [5,10,20,25,24,15,12,6], 
                        title="\\% of population in each age range",
                        labels=["< 10", "10 - 20", "20 - 30", "30 - 40", "40 - 50", "50 - 60", "60 - 70", "> 80"],
                        hlines = [5,10,15,20, 25],
                        hlines_labels = ["5%", "10%", "15%", "20%", "25%"],
                        font_size=15,
                        height=2.5, stroke_width=1,
                        binwidth=0.4, 
                        bingap=0.1,
                        color=BLUE_E, fill_opacity=0.5).move_to([-3,0,0]).move_to(position)
        if transform_from is not None:
            scene.play(Transform(transform_from, h), run_time=5)
        else:
            scene.play(Create(h), run_time=5)
        return h

def play_decision_histogram(scene, position, transform_from=None):
        h = histogram([50,20,30], 
                        title="chances of taking each decision",
                        labels=["run", "movie", "home"],
                        hlines = [20,40,60],
                        hlines_labels = ["20%", "40%", "60%"],
                        font_size=15,
                        height=2.5, stroke_width=1,
                        binwidth=1, 
                        bingap=0.3,
                        color=BLUE_E, fill_opacity=0.5).move_to([-3,0,0]).move_to(position)
        if transform_from is not None:
            scene.play(Transform(transform_from, h), run_time=5)
        else:
            scene.play(Create(h), run_time=5)
        return h

def play_email_histogram(
                scene, 
                position, 
                mu=5, 
                loc=5, 
                binwidth = 0.3,
                show_xlabels = True,
                show_ylabels = True,
                run_time = 5
    ):
    h = poisson_histogram(
                mu=mu, 
                loc=loc, 
                binwidth = binwidth,
                show_xlabels = show_xlabels,
                show_ylabels = show_ylabels,
                title = "\\% of days with each number of received emails",
                x_name = "msgs"
            )
    h = h.move_to(position)
    scene.play(Create(h), run_time=run_time)
    return h

def play_prob_inerpretations(scene):

    t1 = MathTex(r"\text{Interpretations of probability}", font_size=48).move_to([0,0,0])
    t2 = MathTex(r"\text{An estimation from a poll}").next_to(t1, DOWN)
    t3 = MathTex(r"\text{How sure I am of something (run, movie, home)}").next_to(t2, DOWN)
    t4 = MathTex(r"\text{Population exhaustive census}").next_to(t3, DOWN)
    scene.play(Write(t1), run_time=2)
    scene.play(Write(t2), run_time=2)
    scene.play(Write(t3), run_time=2)
    scene.play(Write(t4), run_time=2)
    return VGroup(t1,t2,t3,t4)


class Main(Scene):
    def construct(self):
        video_name = r"distributions and probabilities"
        sfile = find_soundfile('basics-01-discrete-vs-continuous_v2')

        play_intro_scene(self, video_name)
        
        
        timer = SceneTimer(self, debug_wait=False).reset()
        

        self.add_sound(sfile)
        timer.wait_until(10)
        self.play(Write(MathTex(r"P(x) : Domain_x \rightarrow [0,1]", 
                                color=BLUE_E, 
                                font_size=48)
                        .move_to([0,3,0])))

        timer.wait_until(26)
        text_continuous = Text("continuous", color=BLUE_E).move_to([3,2,0])
        self.play(Write(text_continuous))
        timer.wait_until(41)

        text_discrete = Text("discrete", color=BLUE_E).move_to([-3,2,0])
        self.play(Write(text_discrete))
        timer.wait_until(44)

        g = play_professions(self)
        timer.wait_until(58)
        self.play(FadeOut(g))

        g = play_cities_histogram(self, position=[-3,-1,0])
        timer.wait_until("1min 18sec")
        self.play(FadeOut(g))

        g = play_age_histogram(self, position=[-3,-1,0])
        timer.wait_until("1min 24sec")
        self.play(FadeOut(g))

        g = play_decision_histogram(self, position=[-3,-1,0])
        timer.wait_until("1min 34sec")
        self.play(FadeOut(g))

        g = play_email_histogram(self, position=[-3,-1,0])
        timer.wait_until("1min 55sec")
        self.play(FadeOut(g))

        g = play_prob_inerpretations(self)
        timer.wait_until("2min 18sec")
        self.play(FadeOut(g))


        g1 = play_continuous_function(
            self, 
            position = [3.5,-1,0],
            fun = lambda x: stats.beta(a=4, b=2.5).pdf( (x-50)/150), 
            xmin=50, xmax=200, 
            title="population height in cm",
            animation_run_time = 10
        )
        self.wait(3)
        g2 = play_continuous_function(
            self, 
            position = g1.get_center(),
            fun = lambda x: stats.beta(a=15, b=5).pdf( (x-50)/150), 
            transform_from = g1,
            xmin=50, xmax=200, 
            title="population height in cm",
            animation_run_time = 10
        )
        timer.wait_until("2min 54sec")
        self.play(FadeOut(g1), FadeOut(g2))

        g1 = play_continuous_function(
            self, 
            position = [3.5,-1,0],
            fun = lambda x: stats.beta(a=2, b=5).pdf( x/900),
            xmin=0, xmax=900, 
            title="time between emails in secs",
            animation_run_time = 8,
            x_splits = 5
        )
        self.wait(3)
        g2 = play_continuous_function(
            self, 
            position = g1.get_center(),
            transform_from = g1,
            fun = lambda x: stats.beta(a=2, b=10).pdf( x/900),
            xmin=0, xmax=900, 
            title="time between emails in mins",
            animation_run_time = 8,
            x_splits = 5
        )
        timer.wait_until("3min 18sec")
        self.play(FadeOut(g1), FadeOut(g2))        

        timer.wait_until("3min 30sec")
        text_pmf = MathTex(r"\text{Probability Mass Function}").next_to(text_discrete, DOWN*2)
        text_PMF = MathTex(r"\text{PMF}", font_size=48).next_to(text_pmf, DOWN)
        g1 = VGroup(text_pmf, text_PMF)
        self.play(Write(g1))

        timer.wait_until("3min 36sec")
        text_pdf = MathTex(r"\text{Probability Density Function}").next_to(text_continuous, DOWN*2)
        text_PDF = MathTex(r"\text{PDF}", font_size=48).next_to(text_pdf, DOWN)
        g2 = VGroup(text_pdf, text_PDF)
        self.play(Write(g2))

        timer.wait_until("4min 4sec")
        gf = graph_function(
            fun = lambda x: stats.beta(a=4, b=2.5).pdf( (x-50)/150), 
            xmin=50, xmax=200, y_length=2,
            title="population height in cm",
        ).next_to(text_PDF, DOWN*2)
        self.play(Create(gf))

        timer.wait_until("4min 9sec")
        gh = poisson_histogram(x_name="msgs", height=2).next_to(text_PMF, DOWN*2)
        self.play(Create(gh))

        timer.wait_until("4min 20sec")
        self.play(FadeOut(VGroup(gf,gh)))

        timer.wait_until("4min 28sec")
        formula_PMF = MathTex("\sum_i P(x_i) = 1").next_to(text_PMF, DOWN*2)
        self.play(Write(formula_PMF))

        timer.wait_until("4min 32sec")
        formula_PDF = MathTex("\int P(x) dx = 1").next_to(text_PDF, DOWN*2)
        self.play(Write(formula_PDF))

        timer.wait_until("4min 40sec")

        rv     = MathTex(r"\text{Random Variable}").move_to([-4,-2,0])
        rvals  = MathTex(r"\text{Domain (possible values)}").next_to(rv,RIGHT*2)
        rprobs = MathTex(r"\text{Probabilities}").next_to(rvals,RIGHT*2)

        self.play(Write(rv))
        self.play(Write(rvals ))
        self.play(Write(rprobs))

        rv1     = MathTex(r"X = \text{people's height}", font_size=24).next_to(rv, DOWN)
        rvals1  = MathTex(r"x_1, x_2, ... \in [50,250)", font_size=24).next_to(rv1, RIGHT*5)
        rprobs1 = MathTex(r"P(x_1), P(x_2), ... \in [0,1]", font_size=24).next_to(rprobs, DOWN)

        rv2     = MathTex(r"Y = \text{\text{emails per day}", font_size=24).next_to(rv1, DOWN)
        rvals2  = MathTex(r"y_1, y_2, ... \in \mathbb{Z}^+", font_size=24).next_to(rv2, RIGHT*5)
        rprobs2 = MathTex(r"P(y_1), P(y_2), ... \in [0,1]", font_size=24).next_to(rprobs1, DOWN)

        self.play(Write(VGroup(rv1, rvals1, rprobs1)))
        self.play(Write(VGroup(rv2, rvals2, rprobs2)))

        timer.wait_until("5min 5sec")
        self.play(FadeOut(rv, rvals, rprobs, 
                          rv1, rvals1, rprobs1, 
                          rv2, rvals2, rprobs2,
                          formula_PMF, formula_PDF,
                          text_pdf, text_PDF,
                          text_pmf, text_PMF, 
                          text_discrete))

        self.play(text_continuous.animate.move_to([0,2,0]))

        timer.wait_until("5min 18sec")

        g = graph_function(
            fun = lambda x: stats.beta(a=2, b=4).pdf( (x)/5),
            xmin=0, xmax=5, y_length=2,
            x_splits = 5,
            title="time between emails in minutes",
            title_kwargs = {'font_size': 36}
        ).next_to(text_continuous, DOWN*2)
        self.play(Create(g))

        timer.wait_until("5min 20sec")
        axes, graph, _ = g
        ga = fill_graph(self, axes, graph, 0,1)
        
        timer.wait_until("5min 25sec")
        self.play(FadeOut(g, ga))

        g = graph_function(
            fun = lambda x: stats.beta(a=4, b=2.5).pdf( (x-50)/150), 
            xmin=50, xmax=200, y_length=2,
            title="population height in cm",
            title_kwargs = {'font_size': 36}
        ).next_to(text_continuous, DOWN*2)
        self.play(Create(g))
        self.wait(1)
        axes, graph, _ = g
        ga = fill_graph(self, axes, graph, 50, 169)

        timer.wait_until("5min 35sec")
        formula_cdf = MathTex(r"\text{CDF}(x) = \int_{-\infty}^{k}P(x)dx").next_to(g, DOWN)
        self.play(Write(formula_cdf ))

        timer.wait_until("5min 40sec")
        text_cdf = MathTex(r"\text{Cumulative Distribution Function").next_to(formula_cdf, DOWN)
        self.play(Write(text_cdf))
        timer.wait_until("5min 50sec")
        self.play(FadeOut(g, ga, text_cdf, formula_cdf))

        timer.wait_until("5min 55sec")

        g = graph_function(
            fun = lambda x: stats.beta(a=2, b=4).pdf( (x)/5),
            xmin=0, xmax=5, y_length=2,
            x_splits = 11,
            title_kwargs = {'font_size': 36},
            additional_x_axis_config = {'font_size': 18, 'decimal_number_config' : { 'color': '#222222', 'num_decimal_places': 1}},
        ).next_to(text_continuous, DOWN*2)

        self.play(Create(g))
        axes, graph, _ = g
        dot = Dot(axes.c2p(2.32,0), radius=0.05, color=BLACK)
        self.play(Create(dot))

        timer.wait_until("6min 5sec")
        f = graph.underlying_function
        line1 = Line(start=axes.c2p(2.32,0), end=axes.c2p(2.32, f(2.32)), color=BLUE)
        line2 = Line(start=axes.c2p(2.32, f(2.32)), end=axes.c2p(0, f(2.32)), color=BLUE)
        self.play(Create(line1))
        self.play(Create(line2))
        tval = MathTex("1.43").next_to(line2, LEFT )
        self.play(Write(tval))

        timer.wait_until("6min 15sec")
        t1 = MathTex(r"P(x = 2.32) = 1.43").next_to(dot, DOWN*3 + LEFT*2)
        t2 = MathTex(r"\rightarrow \text{used as infinitesimal } dx").next_to(t1, RIGHT)
        t2b = MathTex(r"\text{ not a probability}", font_size=24).next_to(t2, RIGHT)

        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.play(Write(t2b))

        timer.wait_until("6min 35sec")
        ga = fill_graph(self, axes, graph, 1.82, 2.56)
        t3 = MathTex(r"\int_{2.0}^{2.4} P(x)dx = 0.12").next_to(t1, DOWN*2)
        t4 = MathTex(r"\rightarrow \text{a probability of an interval}").next_to(t3, RIGHT)
        self.play(Write(t3))
        self.play(Write(t4))

        timer.wait_until("6min 50sec")
        self.play(FadeOut(t3,t4))
        t3 = MathTex(r"\int_{2.32}^{2.32} P(x)dx = 0").next_to(t1, DOWN*2)
        t4 = MathTex(r"\rightarrow \text{interval of length 0 has probability 0}", font_size=32).next_to(t3, RIGHT)
        self.play(Write(t3))
        self.play(Write(t4))

        timer.wait_until("7min 40sec")
        self.play(FadeOut(t3,t4))
        ga = fill_graph(self, axes, graph, 1.82, 2.56)
        t3 = MathTex(r"\int_{2}^{2.4} P(x)dx = 0.12").next_to(t1, DOWN*2)
        t4 = MathTex(r"\rightarrow \text{a probability of an interval}").next_to(t3, RIGHT)
        self.play(Write(t3))
        self.play(Write(t4))


        timer.wait_until("7min 56sec")
        play_credits(self)
        self.wait(5)

        return