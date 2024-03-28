import tkinter as tk
from tkinter import ttk
import math

class Speedometer(tk.Frame):
    def __init__(self, master, speed_var, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = tk.Canvas(self, width=300, height=270)
        self.canvas.grid(row=0, column=0)
        self.canvas.grid(row=0, column=0)
        self._widget_label_frame = ttk.Frame(self, width=300, height=100)
        self.widget_label = ttk.Label(self._widget_label_frame, text = "Speed (mph)")
        self.widget_label.pack(fill="y")
        self._widget_label_frame.grid(row=1, column=0)

        self.control_frame = ttk.Frame(self, width=40, height=300)
        self.control_frame.grid(row=0, column=1, rowspan=2)

        self.speed_var = speed_var
        self.speed_label = ttk.Label(self.control_frame, textvariable=self.speed_var)

        self.speed_label.place(relx=.5, rely=.9,anchor= tk.CENTER)
        self.speed_scale = tk.Scale(self.control_frame, from_=240, to=0, orient='vertical', command=self.update_speed, length=200, showvalue=False, variable=self.speed_var)
        self.speed_scale.place(relx=.5, rely=.5,anchor= tk.CENTER)
        self.grid_rowconfigure(2, minsize=60)
        self.draw_speedometer()

    def draw_speedometer(self):
        # Draw the outer circle representing the speedometer
        self.canvas.create_oval(50, 50, 250, 250, outline='black', width=2)

        # Draw the arc representing the speed range
        self.canvas.create_arc(50, 50, 250, 250, start=225, extent=90, outline='black', width=2)

        # Draw speed labels along the arc
        for speed in range(0, 260, 20):
            angle = 135 + (speed / 240) * 270
            angle_rad = math.radians(angle)
            x = 150 + 120 * math.cos(angle_rad)
            y = 150 + 120 * math.sin(angle_rad)
            self.canvas.create_text(x, y, text=str(speed), font=('Helvetica', 8))

        init_needle_x = 150 + 100 * math.cos(math.radians(135))
        init_needle_y = 150 + 100 * math.sin(math.radians(135))
        # Draw the needle initially pointing to 0
        self.needle = self.canvas.create_line(150, 150, init_needle_x, init_needle_y, fill='red', width=2)

    def update_speed(self, power):
        # Convert power to angle in degrees
        angle = 135 + (float(power) / 240) * 270

        # Convert angle from degrees to radians
        angle_rad = math.radians(angle)

        # Update the position of the needle
        needle_x = 150 + 100 * math.cos(angle_rad)
        needle_y = 150 + 100 * math.sin(angle_rad)

        self.canvas.coords(self.needle, 150, 150, needle_x, needle_y)

class HeadingIndicatorGUI(tk.Frame):
    def __init__(self, master, heading_var, max_rotation=30, **kwargs):
        super().__init__(master, **kwargs)

        self.canvas = tk.Canvas(self, width=300, height=270)
        self.canvas.grid(row=0, column=0)

        self.heading = heading_var
        self.heading.set(0)  # Initial heading angle

        self.slider = tk.Scale(self, from_=-max_rotation, to=max_rotation, orient=tk.HORIZONTAL, length=200, resolution=1,
                               label="Heading Angle (degrees)")
        self.slider.grid(row=1, column=0)

        self.reset_button = ttk.Button(self, text="Reset Heading", command=self.reset_heading)
        self.reset_button.grid(row=2, column=0)

        self.draw_circle()  # Draw the circle
        self.direction_markers = self.draw_direction_markers()
        self.draw_plane()

        self.rotate_direction_markers(0)

    def draw_circle(self):
        # Draw circle
        self.canvas.create_oval(50, 50, 250, 250, outline="black", width=2)

    def draw_direction_markers(self):
        directions = ["S", "E", "N", "W"]  # Switched positions of E and W
        direction_markers = []
        for i, direction in enumerate(directions):
            angle = i * 90  # Initial angle for N, W, S, E
            x = 150 + 90 * math.cos(math.radians(angle))
            y = 150 - 90 * math.sin(math.radians(angle))
            marker = self.canvas.create_text(x, y, text=direction, font=("Arial", 12, "bold"))
            direction_markers.append(marker)

            # Add degree numbers for other angles (excluding 0, 90, 180, 270 degrees)
            if angle % 90 != 0:
                degree_angle = (i * 90) % 360
                self.canvas.create_text(x, y, text=str(degree_angle), font=("Arial", 10))

        return direction_markers

    def update_direction_markers(self, angle):
        # Rotate direction markers based on the angle
        for i, marker in enumerate(self.direction_markers):
            new_angle = i * 90 - angle
            x = 150 + 90 * math.cos(math.radians(new_angle))
            y = 150 - 90 * math.sin(math.radians(new_angle))
            self.canvas.coords(marker, x, y)

    def draw_plane(self):
        # Clear previous plane
        self.canvas.delete("plane")

        # Get current angle
        angle = self.heading.get()

        # Draw plane body
        body_points = [(150, 140), (140, 150), (160, 150)]
        rotated_body_points = []
        for point in body_points:
            x = point[0] - 150
            y = point[1] - 150
            new_x = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle)) + 150
            new_y = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle)) + 150
            rotated_body_points.append((new_x, new_y))
        self.canvas.create_polygon(rotated_body_points, fill="blue", outline="black", tags="plane")

        # Draw wings
        wing_length = 15
        wing_width = 3
        left_wing = [(140, 150), (130, 150 - wing_length), (140 - wing_width / 2, 150 - wing_length), (140, 150)]
        rotated_left_wing = []
        for point in left_wing:
            x = point[0] - 150
            y = point[1] - 150
            new_x = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle)) + 150
            new_y = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle)) + 150
            rotated_left_wing.append((new_x, new_y))
        self.canvas.create_polygon(rotated_left_wing, fill="blue", outline="black", tags="plane")

        right_wing = [(160, 150), (170, 150 - wing_length), (160 + wing_width / 2, 150 - wing_length), (160, 150)]
        rotated_right_wing = []
        for point in right_wing:
            x = point[0] - 150
            y = point[1] - 150
            new_x = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle)) + 150
            new_y = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle)) + 150
            rotated_right_wing.append((new_x, new_y))
        self.canvas.create_polygon(rotated_right_wing, fill="blue", outline="black", tags="plane")

    def rotate_direction_markers(self, angle):
        # Rotate the direction markers
        self.heading.set(angle)
        speed = abs(self.slider.get()) / 20  # Adjust speed
        self.update_direction_markers(angle)

        # Set the rotation direction and speed based on the slider value
        if self.slider.get() >= 0:
            angle_incr = speed
        else:
            angle_incr = -speed

        # Update angle continuously
        self.master.after(50, self.rotate_direction_markers, (angle - angle_incr) % 360)  # Reverse rotation direction

    def reset_heading(self):
        self.slider.set(0)
