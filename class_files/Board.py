import tkinter as tk
from .Point import Point

# Canvas related
class Board(tk.Canvas):
    def __init__(self, root, width, height, *args, **kwargs):
        tk.Canvas.__init__(self, root, width=width, height=height,
                           *args, **kwargs)
        self.points = []

        self.bind("<Button-1>", self.left_click_event)
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def left_click_event(self, event):
        print(f"You clicked at ({event.x},{event.y})")
        last_point = Point(event.x, event.y)

        self.add_point(last_point)
        self.draw_point(last_point)

    def draw_point(self, p: Point, color="red"):
        x = p.get_x()
        y = p.get_y()
        self.create_oval(x-2, y-2, x+2, y+2, fill=color)

    def add_point(self, p: Point):
        self.points.append(p)

    def starting_triangle_ready(self):
        if len(self.points) < 3:
            return False
        else:
            if len(self.points) == 3:
                p1 = self.points[0]
                p2 = self.points[1]
                x = (p1.get_x() + p2.get_x()) / 2
                y = (p2.get_y() + p2.get_y()) / 2
                starting_point = Point(x, y)
                self.add_point(starting_point)
                self.draw_point(starting_point, "green")

            return True

    def draw_point_from_throw(self, throw: int):
        p1 = self.points[-1]
        p2 = self.points[throw % 3]

        x = (p1.get_x() + p2.get_x()) / 2
        y = (p1.get_y() + p2.get_y()) / 2
        midpoint = Point(x, y)

        self.add_point(midpoint)
        self.draw_point(midpoint)

    def clear_board(self):
        self.points = []
        self.delete('all')
