import random
from manim import *
from numpy import sin

width = 100
height = 100
fps = 30

config.frame_rate = fps
config.background_color = BLACK
config.frame_width = width
config.frame_height = height

number_of_lines = 9
number_of_sticks = 100
t = width / (number_of_lines - 1)
nl = t / 3
t_list = []
d_list = []


class Buffon(Scene):

    def construct(self):

        intro = Text("Buffon's Needle Simulation", font_size=600, stroke_width=5)
        self.play(Write(intro).set_run_time(0.8))
        self.wait(5)
        self.remove(intro)

        intro2 = Text(f"The numerical value is the approximation of PI after {number_of_sticks} randomly generated "
                      f"needles"
                      , font_size=250, stroke_width=0.1)
        self.play(Write(intro2).set_run_time(0.5))
        self.wait(4)
        self.remove(intro2)

        intersect = 0
        total = 0
        k = 0
        for i in range(number_of_lines):
            t_list.append(-(width / 2) + i * t)
            d_list.append(0)

        for i in t_list:
            line = Line([i, height / 2, 0], [i, -height / 2, 0], stroke_width=20, stroke_color=WHITE)
            self.play(GrowFromCenter(line).set_run_time(0.01))

        self.wait()

        for j in range(number_of_sticks):
            x = random.uniform(-width / 2, width / 2)
            y = random.uniform(-height / 2, height / 2)
            angle = random.uniform(-PI / 2, PI / 2)

            needle = Line([x, y - (nl / 2), 0], [x, y + (nl / 2), 0], stroke_width=30)
            total += 1
            for a in range(len(t_list)):
                d_list[a] = t_list[a]

            for a in range(len(t_list)):
                d_list[a] = abs(d_list[a] - x)

            distance = min(d_list)

            if distance < (nl * sin(abs(angle)) / 2):
                needle.stroke_color = PURE_GREEN
                intersect += 1
            else:
                needle.stroke_color = GREY

            self.add(needle.rotate(angle))

            def predict(intersect, total):
                prob = intersect / total
                if intersect > 0:
                    pie = (2 * nl / (prob * t))
                else:
                    pie = 0
                return pie

            pred_pie = round(predict(intersect, total), 4)

            text = DecimalNumber(pred_pie, font_size=700, stroke_width=10)

            bg_rec = BackgroundRectangle(text, fill_color=BLACK, fill_opacity=1, buff=1,background_stroke_color=BLUE,background_stroke_width=10)
            text.add_updater(lambda m: m.set_value(pred_pie))
            text.set_color(BLUE)

            self.add(bg_rec)

            self.add(text)
            self.wait(1 / (fps))

            while k < number_of_sticks - 1:
                self.remove(text, bg_rec)
                k = k + 1
                break

        self.wait(10)
