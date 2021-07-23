from p5 import *
from random import randint, uniform


class branch:
    def __init__(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

    def draw(self, r, g, b):
        stroke(r, g, b)
        stroke_weight(2)
        line(self.x_start, self.y_start, self.x_end, self.y_end)

    def wind(self):
        randomX = uniform(-1, 1)
        randomY = uniform(-1, 1)
        self.x_start += randomX
        self.y_start += randomY
        self.x_end += randomX
        self.y_end += randomY

    def right_child(self):
        direction_x = self.x_end - self.x_start
        direction_y = self.y_end - self.y_start
        new_branch = Vector(direction_x, direction_y)
        new_branch.rotate(PI / randint(4, 8))
        new_branch = new_branch * 0.67
        new_x = self.x_end + new_branch.x
        new_y = self.y_end + new_branch.y
        right = branch(self.x_end, self.y_end, new_x, new_y)
        return right

    def left_child(self):
        direction_x = self.x_end - self.x_start
        direction_y = self.y_end - self.y_start
        new_branch = Vector(direction_x, direction_y)
        new_branch.rotate(-PI / randint(4, 8))
        new_branch = new_branch * 0.67
        new_x = self.x_end + new_branch.x
        new_y = self.y_end + new_branch.y
        left = branch(self.x_end, self.y_end, new_x, new_y)
        return left


angle = 0
tree = []
r = 0
g = 255
b = 255
dice = 0


def setup():
    size(1440, 900)
    root = branch(width / 2, height, width / 2, height - 200)
    tree.append(root)


def draw():
    background(24)

    if mouse_is_pressed:
        g = randint(150, 255)
        r = randint(0, g - 20)
        b = randint(0, g - 20)
        if len(tree) < 300:
            tree_size = len(tree)
            for i in range(0, tree_size):
                if randint(0, 10) < 2:
                    left_child = tree[i].left_child()
                    tree.append(left_child)
                if randint(0, 10) < 2:
                    right_child = tree[i].right_child()
                    tree.append(right_child)
        else:
            tree.clear()
            setup()

    for branch in tree:
        branch.draw(r, g, b)
        # branch.wind()


run()
