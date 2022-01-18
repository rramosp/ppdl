import logging
import os, sys
sys.path.insert(0, "src")

from manim import *
from common.scenes import *
from common.objects import *
from common.utils import *

def play_intro_wheely(scene):
    f1 = Wheely(mode="thinking").scale(0.3).move_to([-2,1,0])

    scene.play(FadeIn(f1))
    f1.play_say(scene, "What is a probability distribution?")

    scene.play(*f1.callout.fadeout_bubble(), ScaleInPlace(f1,0.3))
    scene.play(f1.callout.text.animate.move_to([0,3,0]), f1.animate.to_edge(UL, buff=0.1))

    f1.play_change_mode(scene, "smile")    

def play_intro_video(scene):

    t = Text("what is a probability distribution?", color=BLUE_E).to_edge(UP)
    scene.play(Write(t))
    return t

def play_x2px(scene):
    r = VGroup()

    xs = [MathTex(f"x_{i}") for i in range(5)] + [ MathTex(r"\cdots") ]
    ps = [MathTex(f"P(x_{i})") for i in range(5)] 
    
    k = 1.5
    for i,x in enumerate(xs):
        x = x.move_to([-4 + k*i,2, 0])
        r.add(x)
        scene.play(Write(x), run_time=0.2)

    for i,_ in enumerate(xs[:-1]):
        ar = Arrow(start = [-4 + k*i,2, 0], end = [-4 + k*i,1, 0], color=BLUE_E)
        r.add(ar)
        scene.play(Create(ar), run_time=0.2)

    for i,p in enumerate(ps):
        p = p.move_to([-4 + k*i,1, 0])
        r.add(p)
        scene.play(Write(p), run_time=0.2)

    return r

def play_prob_formulas(scene):

    t1 = MathTex(r"P(x_i) \in [0,1]").move_to([0,0,0])
    scene.play(Write(t1))
    scene.wait(3)

    t2 = MathTex(r"\sum_{i=0}^{n-1}P(x_i) = 1").next_to(t1, DOWN)
    scene.play(Write(t2))
    scene.wait(3)

    t3 = MathTex(r"\int_{-\infty}^{\infty}}P(x) dx = 1").next_to(t2, RIGHT, buff=2)
    scene.play(Write(t3))
    scene.wait(3)

    r = VGroup()
    r.add(t1)
    r.add(t2)
    r.add(t3)
    return r


def play_die_1to6(scene):
    v = VGroup()
    for i in range(6):
        #t = MathTex(r"1\;\;\rightarrow 1/6").move_to([-5,0-i,0])
        t = MathTex(f"{i+1} \\rightarrow 1/6").move_to([-5.2,-0.5-i/2,0])
        v.add(t)
        scene.play(Write(t), run_time=0.3)

    return v

def play_histogram(scene, position):
        h = histogram([5,10,20,25,24,15,12,6], 
                        labels=["< 10", "10 - 20", "20 - 30", "30 - 40", "40 - 50", "50 - 60", "60 - 70", "> 80"],
                        hlines = [5,10,15,20],
                        hlines_labels = ["5%", "10%", "15%", "20%"],
                        font_size=15,
                        height=2.5, stroke_width=1,
                        binwidth=0.3, color=BLUE_E, fill_opacity=0.5).move_to([-3,0,0]).move_to(position)
        scene.play(Create(h), run_time=3)
        return h

def play_model_predict(scene, position=[0,0,0]):

    r = VGroup()

    img = get_imgmobject("radiography").scale(0.3).move_to(position)
    ar0 = Arrow(start = [0,0,0], end = [0,-1,0], color=BLUE_E).next_to(img, DOWN, buff=0)

    t = TextCallout("Model", direction=None).next_to(ar0, DOWN, buff=0)
    ar2 = Arrow(start = [0,0,0], end = [1,-0.5,0], color=BLUE_E).next_to(t, RIGHT, buff=0).shift(DOWN/2)
    ar1 = Arrow(start = [0,0,0], end = [1,0.5,0], color=BLUE_E).next_to(t, RIGHT, buff=0).shift(UP/2)

    t_detect = Text("detected 64%", font_size=18, color=RED_E).next_to(ar1, RIGHT).shift(UP*.2)
    t_no_detect = Text("healthy 36%", font_size=18, color=GREEN_E).next_to(ar2, RIGHT).shift(DOWN*.2)

    for i in [ar0, t, ar1, ar2, t_detect, t_no_detect]:
        r.add(i)

    scene.play(FadeIn(img))
    scene.play(Create(r))
    g = Group()
    g.add(img)
    g.add(r)
    return g


def dice_sum(a,b, equal=True):
    c1 = get_imgmobject(f"die{a}").scale(0.5)
    t  = Text("+").next_to(c1, RIGHT)
    c2 = get_imgmobject(f"die{b}").rotate(np.pi/2).scale(0.5).next_to(t, RIGHT)
    r = Group(c1,t,c2)

    if equal:
        r.add(Text(f"= {a+b}").next_to(c2, RIGHT))

    return r


def play_2_dice(scene, position):

    one_plus_one = dice_sum(1,1).move_to(position).to_edge(LEFT)
    six_plus_six = dice_sum(6,6).next_to(one_plus_one, DOWN).to_edge(LEFT)

    scene.play(FadeIn(one_plus_one))
    scene.play(FadeIn(six_plus_six))

    one_plus_six = dice_sum(1,6, False).next_to(six_plus_six, DOWN, buff=0.5).to_edge(LEFT)
    eq1 = Text("=").next_to(one_plus_six, RIGHT, buff=0.5)
    two_plus_five = dice_sum(2,5, False).next_to(eq1, RIGHT, buff=0.5)
    eq2 = Text("=").next_to(two_plus_five, RIGHT, buff=0.5)
    three_plus_four = dice_sum(3,4, False).next_to(eq2, RIGHT, buff=0.5)
    eq3 = Text("=").next_to(three_plus_four, RIGHT, buff=0.5)

    for i in [one_plus_six, eq1,two_plus_five, eq2, three_plus_four, eq3 ]:
        scene.play(FadeIn(i), run_time=0.5)

    six_plus_one = dice_sum(6,1, False).next_to(one_plus_six, DOWN).to_edge(LEFT)
    eq4 = Text("=").next_to(six_plus_one, RIGHT, buff=0.5)
    five_plus_two = dice_sum(5,2, False).next_to(eq4, RIGHT, buff=0.5)
    eq5 = Text("=").next_to(five_plus_two, RIGHT, buff=0.5)
    four_plus_three = dice_sum(4,3, False).next_to(eq5, RIGHT, buff=0.5)
    eq6 = Text("= 7").next_to(four_plus_three, RIGHT, buff=0.5)

    for i in [six_plus_one, eq4, five_plus_two, eq5, four_plus_three, eq6 ]:
        scene.play(FadeIn(i), run_time=0.5)

    r = Group()
    for i in [one_plus_one, six_plus_six, 
              one_plus_six, eq1, two_plus_five, eq2, three_plus_four, eq3,
              six_plus_one, eq4, five_plus_two, eq5, four_plus_three, eq6]:
        r.add(i)


    return r


def play_parties(scene, position=[0,0,0]):



    h = histogram([5,33, 29, 12, 21], 
                    labels=["Party A  ", "Party B  ", "Party C  ", "Party D  ", "Party E  "],
                    hlines = [5,10,15,20,25,30],
                    hlines_labels = ["5%", "10%", "15%", "20%", "25%", "30%"],
                    font_size=24,
                    height=4, stroke_width=1,
                    binwidth=1, color=RED_E, fill_opacity=0.5).move_to([-3,0,0]).move_to(position)

    scene.play(Create(h), run_time=3)

    return h


def play_rain(scene, position=[0,0,0]):

    r1 = Text("P (").move_to(position)
    r2 = get_imgmobject("rain").scale(0.5).next_to(r1, RIGHT)
    r3 = Text(") = 0.5").next_to(r2, RIGHT)
    g1 = Group(r1, r2, r3)

    s1 = Text("P (").next_to(r1, DOWN*2.5 )
    s2 = get_imgmobject("sun").scale(0.5).next_to(s1, RIGHT)
    s3 = Text(") = 0.5").next_to(s2, RIGHT)
    g2 = Group(s1, s2, s3)

    cr1 = Text("P (").next_to(g1, RIGHT, buff=2)
    cr2 = get_imgmobject("rain").scale(0.5).next_to(cr1, RIGHT)
    cr3 = Text("|").next_to(cr2, RIGHT)
    cr4 = get_imgmobject("cloud").scale(0.5).next_to(cr3, RIGHT)
    cr5 = Text(") = 0.7").next_to(cr4, RIGHT)
    g3 = Group(cr1, cr2, cr3, cr4, cr5)

    cs1 = Text("P (").next_to(g2, RIGHT, buff=2)
    cs2 = get_imgmobject("sun").scale(0.5).next_to(cs1, RIGHT)
    cs3 = Text("|").next_to(cs2, RIGHT)
    cs4 = get_imgmobject("cloud").scale(0.5).next_to(cs3, RIGHT)
    cs5 = Text(") = 0.3").next_to(cs4, RIGHT)
    g4 = Group(cs1, cs2, cs3, cs4, cs5)

    newinfo = Text ("new information", font_size=32).next_to(g3, UP, buff=0.5)
    a1 = MathTex(r"\rightarrow").next_to(g1, buff=1)
    a2 = MathTex(r"\rightarrow").next_to(g2, buff=1)

    scene.play(FadeIn(g1))
    scene.play(FadeIn(g2))
    scene.wait(1)
    scene.play(Write(VGroup(a1,a2)))
    scene.play(Write(newinfo))
    scene.wait(1)
    scene.play(FadeIn(g3))
    scene.play(FadeIn(g4))

    return Group(g1, g2, newinfo, g3, g4, a1, a2)

def play_model_predict_wrong(scene, position= [0,0,0]):

    r = play_model_predict(scene, position)
    a = MathTex(r"\rightarrow").next_to(r, RIGHT, buff=0.5).shift(UP*0.3)
    t = Text("WRONG PREDICTION\nthe patient was healthy!!!", font_size=24, color=RED).next_to(a, RIGHT)

    scene.wait(2)

    scene.play(Write(a), Write(t))

    return Group(r,a, t)

def play_mixed_dataset(scene, position=[0,0,0]):

    g1 = VGroup()
    g2 = VGroup()

    l1 = Circle(.07, color=RED, fill_opacity=0.5).move_to(position+np.r_[[-1,3,0]])
    t1 = Text("patients with pathology", font_size=14).next_to(l1, RIGHT)
    l2 = Circle(.07, color=BLUE, fill_opacity=0.5).next_to(l1, DOWN)
    t2 = Text("healthy patients", font_size=14).next_to(l2, RIGHT)
    legend = VGroup(l1,t1,l2,t2)


    p = np.r_[position]

    c1 = np.random.random(size=(70,2))*4-2 + p[:2]
    c2 = np.random.random(size=(70,2))*4-np.r_[[-0.5,2]] + p[:2]

    for x,y in c1:
        g1.add(Circle(.07, color=RED, fill_opacity=0.5).move_to([x,y,0]))

    for x,y in c2:
        g2.add(Circle(.07, color=BLUE, fill_opacity=0.5).move_to([x,y,0]))

    scene.play(Create(g1))
    scene.play(Create(g2))
    scene.play(FadeIn(legend))
    return VGroup(g1,g2, legend)


def play_nns(scene, position=[0,0,0]):

    circle_kwargs = {"radius":0.2, "fill_opacity": 0.5, "color": BLUE}
    line_kwargs = {"color": GRAY_C, "stroke_width":1 }


    nn1 = neuralnet([3,2], layers_buff=1, 
                circle_kwargs = circle_kwargs,
                line_kwargs = line_kwargs).scale(0.5).move_to(position)

    nn2 = neuralnet([3,5,5,2], layers_buff=1, 
                circle_kwargs = circle_kwargs,
                line_kwargs = line_kwargs).scale(0.5).next_to(nn1, RIGHT, buff=1)

    nn3 = neuralnet([3,5,10,15,5,2], layers_buff=1, 
                circle_kwargs = circle_kwargs,
                line_kwargs = line_kwargs).scale(0.4).next_to(nn2, RIGHT, buff=1)


    t1 = Text("too simple", color=RED_E, font_size=24).next_to(nn1, DOWN)
    t2 = Text("just right", color=RED_E, font_size=24).next_to(nn2, DOWN)
    t3 = Text("too complex", color=RED_E, font_size=24).next_to(nn3, DOWN)

    scene.play(Create(nn1), Write(t1))
    scene.wait(5)
    scene.play(Create(nn2), Write(t2))
    scene.wait(5)
    scene.play(Create(nn3), Write(t3))
    
    return VGroup(nn1,nn2,nn3, t1, t2, t3)

def play_patient_age_to_distribution(scene, position=[0,0,0]):

    number = Text("patient age = 32", color=RED, font_size=32).move_to(position)

    g = gaussian(color=RED).scale(2).move_to(position)
    t = Text("patient age", font_size=24).next_to(g, DOWN)
    g = VGroup(g,t)

    scene.play(Write(number))
    scene.wait(3)
    scene.play(Transform(number, g))
    return number

def play_nn_with_gaussian(scene, position=[0,0,0]):

    circle_kwargs = {"radius":0.2, "fill_opacity": 0.5, "color": BLUE}
    line_kwargs = {"color": GRAY_C, "stroke_width":1 }


    nn = neuralnet([2,1], layers_buff=1, 
                circle_kwargs = circle_kwargs,
                line_kwargs = line_kwargs).scale(3).move_to(position)

    g = gaussian(color=RED).scale(.5).move_to(nn.get_center()+UP)

    scene.play(FadeIn(nn), Create(g))

    return VGroup(nn,g)


def play_nn_with_funcs(scene, position=[0,0,0]):

    circle_kwargs = {"radius":0.2, "fill_opacity": 0.5, "color": BLUE}
    line_kwargs = {"color": GRAY_C, "stroke_width":1 }


    nn = neuralnet([2,3,1], layers_buff=.5, 
                circle_kwargs = circle_kwargs,
                line_kwargs = line_kwargs).scale(2).move_to(position)

    f1 = gaussian(color=RED).scale(.5).move_to(nn.get_center()+UR)
    f2 = function(lambda x: np.exp(-4*(x-1)**2) + .8*np.exp(-5*(x)**2), x_range=(-1,2), color=RED).scale(.5).stretch_to_fit_width(0.5).move_to(nn.get_center()+RIGHT)
    f3 = function(lambda x: np.exp(-(x+1)**2) + .8*np.exp(-5*(x-1)**2), x_range=(-2,2), color=RED).scale(.5).stretch_to_fit_width(0.5).move_to(nn.get_center()+DR)

    fg = VGroup(f1,f2,f3)    
    scene.play(FadeIn(nn), Create(fg))

    return VGroup(nn,fg)

def play_wheely_bye(scene, position=[0,0,0]):
    w = Wheely(mode="smile").scale(0.3).move_to(position)
    scene.play(FadeIn(w))
    scene.wait(10)
    scene.play(*w.rotate_wheel(), *w.change_mode("thinking"))

    return w


def play_transform_func(scene, position=[0,0,0]):

    f1 = gaussian(color=RED).scale(3).move_to(position)
    f2 = function(lambda x: np.exp(-(x+1)**2) + .8*np.exp(-5*(x-1)**2), x_range=(-2,2), color=RED).scale(2).move_to(position).shift(DOWN*0.5)
    f3 = function(lambda x: np.exp(-4*(x-1)**2) + .8*np.exp(-5*(x)**2), x_range=(-1,2), color=RED).scale(2).move_to(position).shift(DOWN*0.5)
    f4 = function(lambda x: np.exp(-10*x**2), x_range=(-1,1), color=RED).scale(2).stretch_to_fit_width(2).move_to(position).shift(DOWN*0.5)

    scene.play(Create(f1))
    scene.wait(2)
    scene.play(Transform(f1, f2))
    scene.wait(2)
    scene.play(Transform(f1, f3))
    scene.wait(2)
    scene.play(Transform(f1, f4))
    return VGroup(f1)

def play_nn_with_gaussian(scene, position=[0,0,0]):

    circle_kwargs = {"radius":0.2, "fill_opacity": 0.5, "color": BLUE}
    line_kwargs = {"color": GRAY_C, "stroke_width":1 }


    nn = neuralnet([2,1], layers_buff=1, 
                circle_kwargs = circle_kwargs,
                line_kwargs = line_kwargs).scale(3).move_to(position)

    g = gaussian(color=RED).scale(.5).move_to(nn.get_center()+UP)

    scene.play(FadeIn(nn), Create(g))

    return VGroup(nn,g)    

class Main(Scene):
    def construct(self):
        video_name = r"talking about probability"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()
        sfile = find_soundfile('thinking_about_probability')

        self.add_sound(sfile)
        intro = play_intro_video(self)
        timer.wait_until(5)
        x2p = play_x2px(self)

        timer.wait_until(12)
        die = play_die_1to6(self)
        
        timer.wait_until(21)
        h = play_histogram(self, [-1,-1.5,0])
        
        timer.wait_until(30)
        r = play_model_predict(self,[3,-1,0])

        timer.wait_until(42)
        self.play(FadeOut(die), FadeOut(h),FadeOut(r))
        forms = play_prob_formulas(self)
        
        timer.wait_until("1min 37sec")
        self.play(FadeOut(forms), FadeOut(x2p))
        self.wait(5)
        twodice = play_2_dice(self, position=[-5,1,0])
        
        timer.wait_until("2min 15sec")
        self.play(FadeOut(twodice))
        self.wait(5)
        parties = play_parties(self, position=[0,-0.5,0])

        timer.wait_until("3min 20sec")
        self.play(FadeOut(parties))
        self.wait(5)
        prain = play_rain(self, [-5,0,0])

        timer.wait_until("4min 10sec")
        self.play(FadeOut(prain))        
        r = play_model_predict_wrong(self,[-3,0,0])

        timer.wait_until("5min 5sec")
        self.play(FadeOut(r), FadeOut(intro))
        tml = Text("Uncertainty in Machine Learning", color=BLUE_E).to_edge(UP)
        self.play(Write(tml))

        timer.wait_until("5min 20sec")
        ds = play_mixed_dataset(self, position=[-1.5,-1,0])

        timer.wait_until("5min 50sec")
        self.play(FadeOut(ds))
        nns = play_nns(self, position=[-4,0,0])

        timer.wait_until("6min 33sec")
        self.play(FadeOut(nns))
        pa = play_patient_age_to_distribution(self)

        timer.wait_until("7min 15sec")
        self.play(FadeOut(pa))
        ng = play_nn_with_gaussian(self)

        timer.wait_until("8min 15sec")
        self.play(FadeOut(ng))
        ff = play_transform_func(self)


        timer.wait_until("9min 00sec")
        self.play(FadeOut(ff))
        self.wait(2)
        
        nf = play_nn_with_funcs(self)
        self.wait(10)
        self.play(nf.animate.move_to([3.5,.5,0]))
        w = play_wheely_bye(self, [-1,-1,0])

        timer.wait_until("9min 35sec")
        self.play(FadeOut(nf, w))

