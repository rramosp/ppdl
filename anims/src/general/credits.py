import logging
import os, sys

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *


class Main(Scene):
    def construct(self):

        play_credits(self)