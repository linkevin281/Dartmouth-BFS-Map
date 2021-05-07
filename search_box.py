# name: Kevin Lin
# date: 03/12/2021
# purpose: create search box class

from cs1lib import *

# Parameters: list is a list of the search characters
# Parameters: x and y are the location of the box / w and h are width and height of the box
# Parameters: size is text font size
# object is a search box
class Searchbox:
    def __init__(self, list, x, y, w, h, size):
        self.list = list
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.str = "".join(list)
        self.size = size

    # draws search box, search text, and "search: " above box
    def draw_box(self, r, g, b):
        enable_stroke()
        set_stroke_color(0, 0, 0)
        set_fill_color(1, 1, 1)
        draw_rectangle(self.x, self.y, self.w, self.h)
        set_font_size(self.size)
        set_stroke_color(r, g, b)
        draw_text(self.str + "|", self.x + 5, self.y + 25)
        set_stroke_color(0, 0, 0)
        set_font_size(self.size * 1.05)
        draw_text(self.str, self.x + 5, self.y + 25)
        set_font_size(25)
        set_stroke_color(0, 0.5, 0)
        draw_text("Search: ", self.x, self.y - 15)

    # draws the start button
    def draw_start(self):
        disable_stroke()
        set_fill_color(0, 0.5, 0)
        draw_circle(self.x + 20, self.y + 140, self.size * 2.5)
        enable_stroke()
        set_stroke_color(0, 0, 0)
        set_font_size(self.size * 0.8)
        draw_text("Set", self.x + 7, self.y + 120)
        draw_text("Location", self.x - 10, self.y + 136)
        set_font_size(self.size * 1.2)
        draw_text("1", self.x + 12, self.y + 165)

    # draws the goal button
    def draw_goal(self):
        disable_stroke()
        set_fill_color(1, 0, 0)
        draw_circle(self.x + 110, self.y + 140, self.size * 2.5)
        enable_stroke()
        set_stroke_color(0, 0, 0)
        set_font_size(self.size * 0.8)
        draw_text("Set", self.x + 97, self.y + 122)
        draw_text("Location", self.x + 80, self.y + 138)
        set_font_size(self.size * 1.2)
        draw_text("2", self.x + 102, self.y + 167)

    # Parameters: mx and my are mouse coordinates
    # tests if the mouse is on the search box
    def on_box(self, mx, my):
        if mx >= self.x and mx <= self.x + self.w:
            if my >= self.y and my <= self.y + self.h:
                return True
        else:
            return False

    # Parameters: mx and my are mouse coordinates
    # tests if the mouse is on the start button
    def on_button_start(self, mx, my):
        if mx >= self.x + 20 - (self.size * 2.5) and mx <= self.x + 20 + (self.size * 2.5):
            if my >= self.y + 140 - (self.size * 2.5) and my <= self.y + 140 + (self.size * 2.5):
                return True
        else:
            return False

    # Parameters: mx and my are mouse coordinates
    # tests if the mouse is on the goal button
    def on_button_goal(self, mx, my):
        if mx >= self.x + 110 - (self.size * 2.5) and mx <= self.x + 110 + (self.size * 2.5):
            if my >= self.y + 140 - (self.size * 2.5) and my <= self.y + 140 + (self.size * 2.5):
                return True
        else:
            return False