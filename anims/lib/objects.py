import os
import logging

import numpy as np
import os
import itertools
import inspect

from manim import *
from manim.constants import *
from manim.mobject.svg.svg_mobject import *
import manim
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

config.background_color = WHITE

def set_if_not_set(dict, key, value):
    if not key in dict.keys():
        dict[key] = value
    return dict

# -------------------------------------
# redefine manim classes with default args

manim_classnames = ["MathTex", "Arrow", "Tex", "Text", "Rectangle", "Line", "DashedLine"]

def set_default_kwargs(class_name, kwargs):
    kwargs = set_if_not_set(kwargs, 'color', BLACK)

    if class_name in ['Text', 'Tex', 'MathTex', 'MarkdownText']:
        kwargs = set_if_not_set(kwargs, 'font_size', 36)

    if class_name in ['Text', 'MarkdownText']:
        kwargs = set_if_not_set(kwargs, 'font', 'sans-serif')

    return kwargs

for classname in manim_classnames:
    exec(f"""
class {classname}(manim.{classname}):
    def __init__(self, *args, **kwargs):
        kwargs = set_default_kwargs("{classname}", kwargs)
        super().__init__(*args, **kwargs)
    
    """)
# ----------------------------------------


def get_imgmobject(name):
    return ImageMobject(find_imgfile(name), image_mode="RGBA")


def get_matplotlibfig(fig):
    fname = "/tmp/xx.png"
    plt.savefig(fname)
    mo = ImageMobject(fname, image_mode="RGBA")
    os.remove(fname)
    return mo

dirs = [os.path.dirname(inspect.getfile(get_imgmobject))+"/../", "/media"]

def find_mediafile(file, media):
    assert media in ['imgs', 'audio']
    fnames = [file] + [f"{file}.{ext}" for ext in ['png', 'jpg', 'gif', 'jpeg', 'wav', 'mp3']]
    tried = []
    for d,f in itertools.product(dirs, fnames):
        fullname = f"{d}/{media}/{f}"
        if os.path.isfile(fullname):
            return fullname
        tried.append(fullname)    
    raise ValueError(f"file {file} not found as {media} anywhere in\n"+"\n".join(tried))

def find_imgfile(file):
    return find_mediafile(file, "imgs")

def find_soundfile(file):
    return find_mediafile(file, "audio")


# -- get the imgs dir as relative to this file (objects.py)
#import inspect
#imgs_dir = os.path.dirname(inspect.getfile(get_imgmobject))+"/../imgs"
#sounds_dir = os.path.dirname(inspect.getfile(get_imgmobject))+"/../audio"

#dirs = [os.path.dirname(inspect.getfile(get_imgmobject)), "/media"]

class Callout(VGroup):

    def __init__(self, message='', direction=DR, margin=0.2, color=BLACK, corner_radius=0.2, font_size=24, **kwargs):
        super().__init__(**kwargs)
        self.message = message
        self.font_size = font_size
        self.color = color
        self.text = self.get_mobject()
        self.margin = margin

        self.bubble = RoundedRectangle(height = self.text.height+self.margin*2, 
                                       width = self.text.width+self.margin*2,
                                       corner_radius = corner_radius,
                                       color = color, stroke_width=1)

        self.add(self.text)
        self.add(self.bubble)

        self.bubble_objects = []
        self.bubble_objects.append(self.bubble)

        if direction is not None:
            self.c1 = Circle(radius=0.15, color=color, stroke_width=1.)\
                          .next_to(self.bubble, direction, buff=0.05)
            self.c2 = Circle(radius=0.05, color=color, stroke_width=1.)\
                          .next_to(self.c1, direction, buff=.07)

            self.add(self.c1)
            self.add(self.c2)
            self.bubble_objects.append(self.c1)
            self.bubble_objects.append(self.c2)


    def get_mobject(self):
        raise NotImplementedError

    def show(self):
        r = [Create(self.bubble), Write(self.text)]

        if "c1" in dir(self):
            r += [Create(self.c1), Create(self.c2)] 

        return r

    def fadeout_bubble(self):
        return [FadeOut(i) for i in self.bubble_objects]

    

class TextCallout(Callout):

    def get_mobject(self):
        return Text(self.message, font_size=self.font_size, color=self.color)        

class TexCallout(TextCallout):

    def get_mobject(self):
        return Tex(self.message, color=self.color, font_size=self.font_size) 

class MathTexCallout(TextCallout):

    def get_mobject(self):
        return MathTex(self.message, color=self.color, font_size=self.font_size) 

class Wheely(Group):

    def __init__(self, mode='smile', **kwargs):
        super().__init__(**kwargs)
        self.mode = mode
        self.wheel = get_imgmobject("wheel")
        self.face  = get_imgmobject(self.mode)
        self.add(self.wheel)
        self.add(self.face)

    def change_mode(self, mode):
        new_self = self.__class__(mode)
        new_self.match_points(self)
        self.mode = mode
        return [Transform(self.face, new_self.face)]

    def play_change_mode(self, scene, mode):
        scene.play(*self.change_mode(mode), *self.rotate_wheel())

    def rotate_wheel(self, angle=np.pi):
        return [Rotate(self.wheel, angle)]

    def say(self, text, ctype=TextCallout, direction=UR, **kwargs):
        assert ctype in [TextCallout, MathTexCallout, TexCallout]

        self.callout = ctype(text, direction=-direction, **kwargs)\
                       .next_to(self, direction, buff=0.)

        return self.callout.show()

    def play_say(self, scene, text, **kwargs):
        scene.play(*self.say(text, **kwargs), *self.rotate_wheel())


def neuralnet(layers, layers_buff=0.5, circle_kwargs={}, line_kwargs={}):

    neurons = VGroup()
    prev_layer = None
    for n in layers:
        gl = VGroup()
        c = Circle(**circle_kwargs)
        gl.add(c)
        for _ in range(n-1):
            new_c = Circle(**circle_kwargs).next_to(c, DOWN)
            c = new_c
            gl.add(c)
        
        if prev_layer is not None:
            gl.next_to(prev_layer, RIGHT, buff=layers_buff)
        prev_layer = gl
        neurons.add(gl)

    # loop over layer objects connectin to the next one
    connections = VGroup()
    for i in range(len(neurons)-1):
        source_layer = neurons[i]
        target_layer = neurons[i+1]
        for source_neuron in source_layer:
            for target_neuron in target_layer:
                l = Line(source_neuron.get_boundary_point(RIGHT), target_neuron.get_boundary_point(LEFT), **line_kwargs)
                connections.add(l)

    return VGroup(neurons, connections)
    
def histogram(bins, 
              labels=None, 
              binwidth=0.5, 
              bingap=0,
              height=4, 
              hlines=None, 
              hlines_labels=None, 
              position=[0,0,0], 
              font_size=24, 
              font_color=BLACK, 
              title = None,
              title_font_size=None,
              **kwargs):

    assert labels is None or len(bins)==len(labels), "must have no labels or one per bin"
    hfactor = height/np.max(bins)
    bp = np.r_[position]
    bw = binwidth
    barwidth = bw - bingap

    xaxis = Line(bp + np.r_[[-bw/2,0,0]], bp + np.r_[[bw*(0.5+len(bins)),0,0]])
    yaxis = Line(bp + np.r_[[0,-bw/2,0]], bp + np.r_[[0,height+bw/2,0]])

    rects = [Rectangle(width=barwidth, height=hfactor*h, **kwargs).move_to(bp+np.r_[[bw*(i+0.5),hfactor*h/2,0]]) for i,h in enumerate(bins)]

    r = VGroup()

    for rect in rects:
        r.add(rect)
    r.add(xaxis)
    r.add(yaxis)
    if labels is not None:
        for i,t in enumerate(labels):
            label = Text(t, font_size=font_size, color=font_color)
            label = label.move_to(bp+np.r_[bw*(i+0.5),-label.width/2-0.2,0]).rotate(np.pi/2) 
            r.add(label)

    if hlines is not None:
        assert hlines_labels is None or len(hlines_labels)==len(hlines), "must have no hlines_labels or one per hline"
        ghlines = VGroup()
        for i,h in enumerate(hlines):
            hline = DashedLine(bp + np.r_[[0,hfactor*h,0]], bp + np.r_[[bw*(0.5+len(bins)),hfactor*h,0]], stroke_width=1, color=GRAY_C)
            ghlines.add(hline)
            if hlines_labels is not None:
                t = Text(hlines_labels[i], font_size=font_size, color=font_color)
                t = t.move_to(bp + np.r_[[-0.05 - t.width, hfactor*h, 0]])
                ghlines.add(t)
        r.add(ghlines)

    if title is not None:
        if title_font_size is None:
            title_font_size = font_size

        t = MathTex(r"\text{"+title+"}", font_size=24)
        t = t.next_to(r, UP)
        r.add(t)

    return r


def function(func, x_range, **kwargs):
    hd = np.r_[.1,0,0]
    vd = np.r_[0,.1,0]
    g = FunctionGraph(func, x_range=x_range, **kwargs)


    bl = g.get_corner(DL)
    br = g.get_bottom() + g.get_right()
    tr = g.get_top() + g.get_right()

    xaxis = Line(g.get_corner(DL)-hd, g.get_corner(DR)+hd, color=BLACK, stroke_width=1)
    yaxis = Line(g.get_corner(DL)-vd, g.get_corner(UL)+vd, color=BLACK, stroke_width=1)
    r =  VGroup(g,xaxis,yaxis)

    return r



def get_axes(
        xmin, 
        xmax, 
        ymin, 
        ymax,
        x_length = 4,
        y_length = 3,
        xlabel = "", 
        xlabel_kwargs = {},
        additional_x_axis_config={},
        additional_y_axis_config={},
        x_splits = 4,
        y_splits = 4,
        show_y_numbers = False
    ):
        
    x_range = [xmin, xmax, (xmax-xmin)/(x_splits-1)]
    y_range = [ymin, ymax, (ymax-ymin)/(y_splits-1)]

    x_axis_config = {
                'numbers_with_elongated_ticks' : np.linspace(xmin, xmax, x_splits),
                'include_numbers' : True,
                'font_size' : 24,
                'color' : BLACK,
                'numbers_to_include' : np.linspace(xmin, xmax, x_splits),
                'longer_tick_multiple' : 2,
                'tick_size': .03,
                'decimal_number_config' : { 
                    'color': '#222222',
                    'num_decimal_places': 0
                }
            }

    y_axis_config = {
                'include_numbers' : False,
                'color' : BLACK,
                'tick_size': .03,
    }

    if show_y_numbers:
        y_axis_config.update({
                'font_size' : 24,
                'include_numbers' : True,
                'numbers_to_include' : np.linspace(ymin, ymax, y_splits),
                'numbers_with_elongated_ticks' : np.linspace(ymin, ymax, y_splits),
                'decimal_number_config' : { 
                    'color': '#222222',
                    'num_decimal_places': 0
                }
            }
        )

    x_axis_config.update(additional_x_axis_config)            
    y_axis_config.update(additional_y_axis_config)            

    axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            tips = False,
            x_axis_config = x_axis_config,
            y_axis_config = y_axis_config

        )

    xlabel_mobject = Tex(xlabel, **xlabel_kwargs).next_to(axes, DOWN)
    g = VGroup(axes, xlabel_mobject)

    return g

class TransformFunction(Animation):
    def __init__(self, plane, get_function_for_value, start: float, end: float, **kwargs) -> None:
        """
        plane: the plane (Axes, NumberPlane, etc.) that holds the function graph
        get_function_for_value: a function that returns a the function to plot for each
                                value of the animation between start and end
        """
        # Pass number as the mobject of the animation
        self.plane = plane
        self.function_graph = self.plane.plot(get_function_for_value(start), color=RED)
        super().__init__(self.function_graph,  **kwargs)
        self.start = start
        self.end = end
        self.get_function_for_value = get_function_for_value
        self.inverse = False

    def switch_direction(self):
        self.inverse = False if self.inverse else True

    def interpolate_mobject(self, alpha: float) -> None:
        if self.inverse:
            alpha = 1-alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.function =lambda x: [x, self.get_function_for_value(value)(x),0]
        self.mobject.clear_points()
        self.mobject.init_points()
        self.mobject.points = np.r_[[self.plane.coords_to_point(*p) for p in self.mobject.points]]

class CountAnimation(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end
        self.inverse = False

    def switch_direction(self):
        self.inverse = False if self.inverse else True

    def interpolate_mobject(self, alpha: float) -> None:
        if self.inverse:
            alpha = 1-alpha
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


def graph_function(
        fun, 
        xmin, 
        xmax, 
        ymin = None, 
        ymax = None,
        x_length = 4,
        y_length = 3,
        title = "", 
        title_kwargs = {},
        additional_x_axis_config={},
        additional_y_axis_config={},
        x_splits = 4,
        y_splits = 4,
        graph_color = BLACK,
        show_y_numbers = False
    ):
    
    xr = np.linspace(xmin, xmax, 100)

    if ymin is None or ymax is None:
        ymin, ymax = np.min(fun(xr)), np.max(fun(xr))
    
    x_range = [xmin, xmax, (xmax-xmin)/(x_splits-1)]
    y_range = [ymin, ymax, (ymax-ymin)/(y_splits-1)]

    x_axis_config = {
                'numbers_with_elongated_ticks' : np.linspace(xmin, xmax, x_splits),
                'include_numbers' : True,
                'font_size' : 24,
                'color' : BLACK,
                'numbers_to_include' : np.linspace(xmin, xmax, x_splits),
                'longer_tick_multiple' : 2,
                'tick_size': .03,
                'decimal_number_config' : { 
                    'color': '#222222',
                    'num_decimal_places': 0
                }
            }

    y_axis_config = {
                'include_numbers' : False,
                'color' : BLACK,
                'tick_size': .03,
    }

    if show_y_numbers:
        y_axis_config.update({
                'font_size' : 24,
                'include_numbers' : True,
                'numbers_to_include' : np.linspace(ymin, ymax, y_splits),
                'numbers_with_elongated_ticks' : np.linspace(ymin, ymax, y_splits),
                'decimal_number_config' : { 
                    'color': '#222222',
                    'num_decimal_places': 2
                }
            }
        )

    x_axis_config.update(additional_x_axis_config)            
    y_axis_config.update(additional_y_axis_config)            

    axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            tips = False,
            x_axis_config = x_axis_config,
            y_axis_config = y_axis_config

        )


    # Create Graph
    graph = axes.plot(fun)
    graph.set_color(graph_color)

    title = Tex(title, **title_kwargs).next_to(axes, DOWN*2)
    g = VGroup(axes, graph, title)

    return g



def poisson_histogram(
                mu=5, 
                loc=5, 
                binwidth = 0.3,
                bingap = 0.1,
                color = BLUE_E,
                fill_opacity = 0.5,
                font_size = 15,
                stroke_width = 1,
                show_xlabels = True,
                show_ylabels = True,
                height = 2.5,
                title = None,
                x_name = ""
    ):

    s = stats.poisson(mu=mu, loc=loc).rvs(10000)
    s = (pd.Series(s).value_counts()/len(s)*100).sort_index()
    labels = [f"{i} {x_name}" for i in s.index]
    vals = list(s.values)

    hlines = np.linspace(0,100,21)[1:]
    hlines = hlines[hlines<s.max()]
    hlines_labels = [f"{i:.0f}%" for i in hlines]

    h = histogram(vals, 
                    title=title,
                    labels=labels if show_xlabels else None,
                    hlines = hlines if show_ylabels else None,
                    hlines_labels = hlines_labels if show_ylabels else None,
                    font_size=font_size,
                    height=height, 
                    stroke_width=stroke_width,
                    binwidth=binwidth,
                    bingap=bingap, 
                    color=color, fill_opacity=fill_opacity)
    return h


def add_brackets(mobj):
    bracket_pair = Tex("\\big[", "\\big]")
    bracket_pair.scale(2)
    bracket_pair.stretch_to_fit_height(
        mobj.get_height() + 2 * 0.1
    )
    l_bracket, r_bracket = bracket_pair.split()
    l_bracket.next_to(mobj, LEFT, .2)
    r_bracket.next_to(mobj, RIGHT, .2)
    return VGroup(l_bracket, mobj, r_bracket)

def updating_animation(mobject,scene,color=BLUE_E, time_width=3):
    scene.play(Circumscribe(mobject,color=color,time_width=time_width,fade_out=True))
    scene.play(Circumscribe(mobject,color=color,time_width=time_width,fade_out=True))
    scene.play(Circumscribe(mobject,color=color,time_width=time_width))


def fill_graph(scene, axes, graph, from_value, to_value, run_time=2):
    area = axes.get_area(graph, [from_value,from_value], color=BLUE, fill_opacity=0.5)
    scene.add(area)

    moving_area = lambda:  axes.get_area(graph, [from_value,tracker.get_value()], color=BLUE, fill_opacity=0.5)
    tracker = ValueTracker(from_value)
    redraw = always_redraw(moving_area)
    scene.add(redraw)
    scene.play(tracker.animate.set_value(to_value), rate_func=smooth, run_time=run_time)
    return redraw

def gaussian(color=RED):
    g = graph_function(fun = lambda x: stats.norm(loc=40, scale=10).pdf(x), 
                       xmin=0, 
                       xmax=80, 
                       y_length=2,
                       x_length=3,
                       graph_color = color,
                       x_splits = 5,
                       additional_x_axis_config = {'tick_size': 0, 
                                                   'include_numbers': False, 
                                                   'numbers_with_elongated_ticks': None, 
                                                   'numbers_to_include': None},
                       additional_y_axis_config = {'tick_size': 0}

            )    
    return g


def generate_stickman(size = 1.0,fill_opacity=0.0 ,general_color = BLACK, color_head = BLACK,
                     color_torso = BLACK, color_left_arm = BLACK,
                     color_right_arm = BLACK, color_left_leg = BLACK, color_right_leg = BLACK
                     ):

    """
    A representation of a person using simple shapes. 

    Will be converted to a stand alone class  if later its needed to implement custom animations for stickmans

    returns: a VDict with each bodypart of the stickman. Bodyparts pairs below

            *   pairs = [ 
                ("head", stickman_head) ,
                ("torso", stickman_torso) ,
                ("left arm", stickman_left_arm),
                ("right arm", stickman_right_arm), 
                ("left leg", stickman_left_leg), 
                ("right leg", stickman_right_leg)
                ]

    function variables:

    size: default 1.0 - represents the general scale of the generated stickman
    color: default BLACK - the general color used for all body parts of the stickman.
    
    The rest of the variables are self explanatory, if you want to change the color of a specific body part just provide a color

    i.g: generate_stickman(color_head = RED,fill_opacity=0.5)
    """

    if general_color != BLACK:
        color_head = general_color
        color_torso = general_color
        color_left_arm = general_color
        color_right_arm = general_color
        color_left_leg = general_color
        color_right_leg = general_color
    
    stickman_head = Circle(radius = 0.5, color= color_head, fill_opacity = fill_opacity)

    ref_point_torso = Dot().move_to(stickman_head.get_bottom()).shift(DOWN)
    ref_point_left_leg = Dot().move_to(ref_point_torso).shift(DOWN+LEFT)
    ref_point_right_leg = Dot().move_to(ref_point_torso).shift(DOWN+RIGHT)

    stickman_torso = Line(start=stickman_head.get_bottom(),end=ref_point_torso.get_center(),buff=0, color=color_torso)

    ref_point_left_arm = Dot().move_to(stickman_torso.get_center()).shift(DOWN*(0.7)+LEFT*(0.7))
    ref_point_right_arm = Dot().move_to(stickman_torso.get_center()).shift(DOWN*(0.7)+RIGHT*(0.7))


    stickman_left_arm = Line(start=stickman_torso.get_center()+UP*size, end = ref_point_left_arm, buff = 0, color = color_left_arm)
    stickman_right_arm = Line(start=stickman_torso.get_center()+UP*size, end = ref_point_right_arm, buff = 0, color = color_right_arm)

    stickman_left_leg = Line(start=stickman_torso.get_end(), end=ref_point_left_leg, buff= 0, color= color_left_leg)
    stickman_right_leg = Line(start = stickman_torso.get_end(), end = ref_point_right_leg, buff = 0, color = color_right_leg)



    pairs = [ 
        ("head", stickman_head) ,
        ("torso", stickman_torso) ,
        ("left arm", stickman_left_arm),
        ("right arm", stickman_right_arm), 
        ("left leg", stickman_left_leg), 
        ("right leg", stickman_right_leg)
        ]

    stickman_vdict = VDict(pairs)

    stickman_vdict.scale(size)

    return stickman_vdict

def get_cancel_line(mobject, color=BLACK):
    """
    Returns a Line Mobject that goes from the left corner of a Mobject up to
    the right corner of that same mobject.

    Useful to show the simplification of fractions/equations

    Default color: BLACK
    
    """

    return Line(start=mobject.get_corner(DL), end=mobject.get_corner(UR), color=color  )