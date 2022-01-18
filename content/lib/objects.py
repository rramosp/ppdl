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


dirs = [os.path.dirname(inspect.getfile(get_imgmobject))+"/../", "/media"]

def find_mediafile(file, media):
    assert media in ['imgs', 'audio']
    fnames = [file] + [f"{file}.{ext}" for ext in ['png', 'jpg', 'gif', 'jpeg', 'wav']]
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
    
def histogram(bins, labels=None, binwidth=0.5, height=4, hlines=None, hlines_labels=None, position=[0,0,0], font_size=24, font_color=BLACK, **kwargs):

    assert labels is None or len(bins)==len(labels), "must have no labels or one per bin"
    hfactor = height/np.max(bins)
    bp = np.r_[position]
    bw = binwidth

    xaxis = Line(bp + np.r_[[-bw/2,0,0]], bp + np.r_[[bw*(0.5+len(bins)),0,0]])
    yaxis = Line(bp + np.r_[[0,-bw/2,0]], bp + np.r_[[0,height+bw/2,0]])

    rects = [Rectangle(width=bw, height=hfactor*h, **kwargs).move_to(bp+np.r_[[bw*(i+0.5),hfactor*h/2,0]]) for i,h in enumerate(bins)]

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

def gaussian(**kwargs):
    return function(lambda x: 3*np.exp(-x**2), x_range=(-2,2), **kwargs).scale(1/3)