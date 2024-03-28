import tkinter as tk
from tkinter import ttk
import math
from cpeworkshop.graphics import GUICanvas, GAirplane, GImage, GraphicsObject
from cpeworkshop.widget import Speedometer, HeadingIndicatorGUI
from tkinter import DoubleVar, IntVar

# # Create the main window
class Application(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Ex1 Set the title of the window to "Airplane Simulation"
        self.title(None)

        # Hint: If you want to set the title to some text, for example,
        #       "Hello, World!", use the syntax below:
        #
        #       self.title("Hello, World!")
        #
        # - You should put a string inside the parenthesis ()
        # - Do not forget the quotation marks ""


        # Ex2 Set the size and width of a window to 700 and the width to 820
        self.geometry(None)

        # Hint: If you want to set the width of a window to 500 and height to
        #       300, use the syntax below:
        #
        #       self.geometry("500x300")
        #
        # - Do not forget the quotation marks ""

        content = tk.Frame(self)
        content.pack()

        airplane_speed = IntVar()
        airplane_heading = DoubleVar()


        # Ex3 Change the background color of the canvas
        # Hint: change argument of GUICanvas
        self.canvas = GUICanvas(content, background = "white", width=680, height=400, borderwidth=2)
        self.canvas.grid(column=0, row=0, columnspan=2)


        speedometer = Speedometer(
            content,
            speed_var = airplane_speed,
            width=300,
            height=360
        )

        # Ex4 Specify the position of speedometer to the first column and
        #     second row
        #
        # Hint: Python index start with zero (0)
        #       To assign the widget to the second column and third row,
        #       set column=3 (not 2)
        speedometer.grid(column=None, row=None)

        # Ex5 Set the maximum rotation speed to 30 degrees/second
        # Hint: To set the maximum rotation speed to m degrees/second
        #       ("m" is a variable), set the value of max_rotation to m
        #
        #       max_rotation = m
        #
        headingindicator = HeadingIndicatorGUI(
            content,
            heading_var=airplane_heading,
            max_rotation=None,
            width=300,
            height=360,
            borderwidth=2
        )


        headingindicator.grid(column=1, row=1)

        # Ex6 Set the color of airplane to your favorite color
        # Hint: To set color of GAirplane
        #       ("c" is a variable), set the value of color to c
        #
        #       color = c
        airplane = GAirplane((340,200), airplane_speed, airplane_heading, color=None)
        self.map = GImage("map.jpg")

        self.canvas.add_graphics(airplane)

    # Ignore
    def add_map(self):
        self.canvas.create_image(0, 0, anchor="nw", image=self.map.get_image(), tags=("map",))


if __name__ == "__main__":
    application = Application()
    application.add_map()
    application.mainloop()
