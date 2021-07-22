from p5 import *
from random import randrange


class branch:
    def __init__(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

    def draw_branch(self, r, g, b):
        stroke(r, g, b)
        line(self.x_start, self.y_start, self.x_end, self.y_end)


angle = 0
tree = []
r = 0
g = 255
b = 255


def setup():
    size(1200, 1200)


def draw():
    background(51)
    root = branch(width / 2, height, width / 2, height - 100)
    if mouse_is_pressed:
        r = randrange(255)
        g = randrange(255)
        b = randrange(255)

    root.draw_branch(r, g, b)


run()
