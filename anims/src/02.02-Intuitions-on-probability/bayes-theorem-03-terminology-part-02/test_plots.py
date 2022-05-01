from __future__ import division
from gzip import WRITE
import logging
import os, sys
from unicodedata import decimal
from unittest import result

from numpy import vdot
from scipy.fftpack import shift

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
import math

sys.path.insert(0, ".")




class Main(Scene):
    def construct(self):
        
        self.camera.background_color = BLACK

        ax = Axes(
            x_range=[0,10,0.5],
            y_range=[0, 10,0.5],
            x_length=1.8,
            y_length=2.5,
            axis_config={"include_tip": False},
        )

       

        plot = ax.plot(lambda x: np.abs(16.5/x) , x_range=[16.5/10,10,0.1],color=BLUE_E)
        
        #number_plane.stroke_color = RED_E














        self.play(FadeIn(ax),FadeIn(plot))

""""
ax = Axes(
            x_range= [0, 0.15, 0.05], 
            y_range= [0, 0.165, 0.05] ,
            x_length=1.5,
            y_length=2,
            axis_config={
                "font_size": 20
            },
            x_axis_config={
                "include_ticks":True,
                "include_tip": False,
                "stroke_color": RED_E,
                "include_numbers": True,

            },
            
            y_axis_config={
                "include_ticks": True,
                "include_tip": False,
                "numbers_to_include": np.arange(0.150, 0.165,0.05),
                "stroke_color": RED_E
            }
            

        ).add_coordinates()"""