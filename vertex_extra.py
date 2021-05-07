# name: Kevin Lin
# date: 03/08/21
# purpose: define vertex class

from cs1lib import *

VERTEX_RADIUS = 10
EDGE_SIZE = 3

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_list = []

    # draws a circle based off rgb parameters and the self.x/y
    def vertex_draw(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # draws a line between one vertex and another
    def edges_draw_between(self, r, g, b, vertex):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_SIZE)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    # draws a line between this vertex and every adjacent vertex
    def edges_draw_all(self, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_SIZE)
        for i in self.adj_list:
            draw_line(self.x, self.y, i.x, i.y)

    # checks if the mouse is within a box around the drawn vertex circle
    def on_vertex(self, x, y):
        if x >= self.x - VERTEX_RADIUS and x <= self.x + VERTEX_RADIUS:
            if y >= self.y - VERTEX_RADIUS and y <= self.y + VERTEX_RADIUS:
                enable_stroke()
                set_stroke_color(1, 0, 0)
                set_font_size(22)
                draw_text(self.name, self.x - 30, self.y - 20)
                return True
        else:
            return False

    def search_display(self):
        enable_stroke()
        set_stroke_color(0, 0, 0)
        set_font_size(22)
        draw_text(self.name, self.x - 30, self.y - 20)

    def __str__(self):
        temp_list = []
        temp_str = ", "
        for i in self.adj_list:
            temp_list.append(i.name)
        adj_names = temp_str.join(temp_list)

        return self.name #+ "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + \
              # adj_names