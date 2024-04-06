import tkinter as tk
from tkinter import ttk
import abc
from typing import Union, List, Dict
import math
from PIL import Image, ImageTk

class GUICanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._graphics_objs = []
        self.after(16, self.draw)

    def add_graphics(self, graphics_obj) -> None:
        self._graphics_objs.append(graphics_obj)

    def draw(self):
        for obj in self._graphics_objs:
            obj.draw(self)
        self.after(60, self.draw)


class GraphicsObject(object):
    def __init__(self):
        pass

    def draw(self, canvas):
        raise NotImplementedError("This is an abstract graphics object class. You must implement draw() in a subclass.")

class GImage(GraphicsObject):
    def __init__(self, imagepath):
        try:
            self.image = ImageTk.PhotoImage(Image.open(imagepath).resize((1020, 600)))
        except:
            self.image = None
            print("WARNING: Error loading image")

    def draw(self, canvas):
        canvas.create_image(0, 0, anchor="nw", image=self.image)
        
    def get_image(self):
        return self.image

class GAirplane(GraphicsObject):
    def __init__(self, origin, speed, direction, color):
        super().__init__()
        self._speed = speed
        self._direction = direction
        self._x = origin[0]
        self._y = origin[1]
        self.color = color
        points = [
            (0,0),
            (2,2),
            (10,2),
            (16,10),
            (18,10),
            (14,2),
            (20,1.7),
            (22,4),
            (23.5,4),
            (22.5,0)
        ]
        points = points + list(reversed([(x, -y) for x, y in points[:-1]]))
        self.points = [(x*3 - 36, y*3) for x, y in points]

    def __str__(self):
        return "airplane"

    def _rotate(self, _angle, points):
        angle = math.radians(_angle.get())
        cos_val = - math.cos(angle)
        sin_val = math.sin(angle)
        new_points = []
        for x, y in points:
            new_x = x * cos_val - y * sin_val
            new_y = x * sin_val + y * cos_val
            new_points.append((new_x, new_y))
        return new_points

    def _translate(self, points, x, y):
        return [(x + x1, y + y1) for x1, y1 in points]

    def _update_position(self):
        self._x += self._speed.get() * math.cos(math.radians(self._direction.get())) / 60
        self._y -= self._speed.get() * math.sin(math.radians(self._direction.get())) / 60

    def draw(self, canvas):
        self._update_position()
        canvas.delete("airplane")
        points = self._translate(self._rotate(self._direction, self.points), self._x, self._y)
        canvas.create_polygon(points, outline="white", width=2, fill=self.color, tags=("airplane",))
