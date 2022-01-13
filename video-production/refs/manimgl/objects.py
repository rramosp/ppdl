from manim import *
import numpy as np

class Speedometer(VMobject):
    CONFIG = {
        "arc_angle": 4 * np.pi / 3,
        "num_ticks": 8,
        "tick_length": 0.2,
        "needle_width": 0.1,
        "needle_height": 0.8,
        "needle_color": YELLOW,
    }

    def init_points(self):
        start_angle = np.pi / 2 + self.arc_angle / 2
        end_angle = np.pi / 2 - self.arc_angle / 2
        self.add(Arc(
            start_angle=start_angle,
            angle=-self.arc_angle
        ))
        tick_angle_range = np.linspace(start_angle, end_angle, self.num_ticks)
        for index, angle in enumerate(tick_angle_range):
            vect = rotate_vector(RIGHT, angle)
            tick = Line((1 - self.tick_length) * vect, vect)
            label = Tex(str(10 * index))
            label.set_height(self.tick_length)
            label.shift((1 + self.tick_length) * vect)
            self.add(tick, label)

        needle = Polygon(
            LEFT, UP, RIGHT,
            stroke_width=0,
            fill_opacity=1,
            fill_color=self.needle_color
        )
        needle.stretch_to_fit_width(self.needle_width)
        needle.stretch_to_fit_height(self.needle_height)
        needle.rotate(start_angle - np.pi / 2, about_point=ORIGIN)
        self.add(needle)
        self.needle = needle

        self.center_offset = self.get_center()

    def get_center(self):
        result = VMobject.get_center(self)
        if hasattr(self, "center_offset"):
            result -= self.center_offset
        return result

    def get_needle_tip(self):
        return self.needle.get_anchors()[1]

    def get_needle_angle(self):
        return angle_of_vector(
            self.get_needle_tip() - self.get_center()
        )

    def rotate_needle(self, angle):
        self.needle.rotate(angle, about_point=self.get_center())
        return self

    def move_needle_to_velocity(self, velocity):
        max_velocity = 10 * (self.num_ticks - 1)
        proportion = float(velocity) / max_velocity
        start_angle = np.pi / 2 + self.arc_angle / 2
        target_angle = start_angle - self.arc_angle * proportion
        self.rotate_needle(target_angle - self.get_needle_angle())
        return self
