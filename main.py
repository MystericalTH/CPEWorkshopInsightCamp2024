import tkinter as tk
from cpeworkshop.graphics import GUICanvas, GAirplane, GImage
from cpeworkshop.widget import Speedometer, HeadingIndicator
from tkinter import DoubleVar, IntVar

# # Create the main window
class Application(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Ex1 Set the title of the window to "Airplane Simulation"
        # 
        # Hint: If you want to set the title to some text, for example,
        #       "Hello, World!", use the syntax below:
        #
        #       self.title("Hello, World!")
        #
        # - You should put a string inside the parenthesis ()
        # - Do not forget the quotation marks ""
        
        self.title(None)                                    #TODO Ex1


        # Ex2 Set the width of the window to 700 and height to 820
        # 
        # Hint: If you want to set the width of a window to 500 and height to
        #       300, use the syntax below:
        #
        #       self.geometry("500x300")
        #
        # - Do not forget the quotation marks ""
        
        self.geometry(None)                                 #TODO Ex2


        content = tk.Frame(self)
        content.pack()

        airplane_speed = IntVar()
        airplane_heading = DoubleVar()


        # Ex3 Change the background color of the canvas to white
        # 
        # Hint: The following code set background color to pink
        # 
        #       background = “pink”
        # 
        # - Do not forget the quotation marks ""
        
        self.canvas = GUICanvas(content, background=None,   #TODO Ex3
                                width=680, height=400, 
                                borderwidth=2)
        
        
        self.canvas.grid(column=0, row=0, columnspan=2)
        speedometer = Speedometer(
            content,
            speed_var = airplane_speed,
            width=300,
            height=360
        )

        # Ex4 Specify the position of a speedometer to the first column and
        #     second row
        #
        # Hint: Python number count start with zero (0)
        #       To assign the widget to the second column and third row
        #       
        #       widget.grid(column=1, row=2)
        # 
        #       and NOT widget.grid(column=2, row=3)
        
        speedometer.grid(column=None, row=None)             #TODO Ex4


        # Ex5 Set the maximal rotation speed to 30 degrees/second
        # 
        # Hint: To set the maximum rotation speed to m degrees/second
        #       ("m" is a variable), set the value of max_rotation to m
        #
        #       ...
        #       max_rotation = 10 # this sets the maximal rotation speed 
        #       ...               # to 10 degrees/second
        # 

        headingindicator = HeadingIndicator(
            content,
            heading_var=airplane_heading,
            max_rotation=None,                              #TODO Ex5
            width=300,
            height=360,
            borderwidth=2
        )


        # Ex6 Specify the position of a heading indicator to 
        #     the second column and second row
        # 
        # Hint: Python number count start with zero (0)
        #       To assign the widget to the second column and third row
        #       
        #       widget.grid(column=1, row=2)
        # 
        #       and NOT widget.grid(column=2, row=3)

        headingindicator.grid(column=None, row=None)        #TODO Ex6


        # Ex7 Set the color of airplane to your favorite color
        # 
        # Hint: To set color of GAirplane
        #       ("c" is a variable), set the value of color to c
        #
        #       color = "black" # this sets the color of the airplane to black
        #
        # - Do not forget the quotation mark ""
        
        airplane = GAirplane((340,200), 
                             airplane_speed, 
                             airplane_heading,
                             color=None)                    #TODO Ex7
        
        
        # Ex8 (extra) Draw map on the canvas by adding filename to GImage
        # 
        # Hint: To draw an image in the background, simply apply the following 
        #       syntax (note that there is a file “map.jpg” in the folder)
        # 
        #       self.map = GImage("filename.jpg")
        # 
        # - Do not forget the quotation mark ""
        
        self.map = GImage(None)                             #TODO Ex8


        self.canvas.add_graphics(airplane)

    # Ignore
    def add_map(self):
        if hasattr(self, "map") and self.map is not None and self.map.get_image() is not None:
            self.canvas.create_image(0, 0, anchor="nw", image=self.map.get_image(), tags=("map",))


if __name__ == "__main__":
    application = Application()
    application.add_map()
    application.mainloop()
