import tkinter as tk


class CircleGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Circle Calculator")
        self.radius_var = tk.StringVar(value="0")
        self.diameter_var = tk.StringVar(value="0")

        # create input widgets
        radius_label = tk.Label(self.root, text="Radius:")
        radius_entry = tk.Entry(self.root, textvariable=self.radius_var)
        diameter_label = tk.Label(self.root, text="Diameter:")
        diameter_entry = tk.Entry(self.root, textvariable=self.diameter_var)

        # create output labels
        area_label = tk.Label(self.root, text="Area:")
        self.area_var = tk.StringVar(value="0")
        area_output = tk.Label(self.root, textvariable=self.area_var)
        perimeter_label = tk.Label(self.root, text="Perimeter:")
        self.perimeter_var = tk.StringVar(value="0")
        perimeter_output = tk.Label(self.root, textvariable=self.perimeter_var)

        # create calculate button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)

        # layout input widgets
        radius_label.grid(row=0, column=0)
        radius_entry.grid(row=0, column=1)
        diameter_label.grid(row=1, column=0)
        diameter_entry.grid(row=1, column=1)

        # layout output labels
        area_label.grid(row=2, column=0)
        area_output.grid(row=2, column=1)
        perimeter_label.grid(row=3, column=0)
        perimeter_output.grid(row=3, column=1)

        # layout calculate button
        calculate_button.grid(row=4, column=1)

        self.root.mainloop()

    def calculate(self):
        radius = float(self.radius_var.get())
        diameter = float(self.diameter_var.get())
        if radius != 0:
            circle = Circle(radius=radius)
        elif diameter != 0:
            circle = Circle(diameter=diameter)
        else:
            return
        area = circle.area()
        perimeter = circle.perimeter()
        self.area_var.set(f"{area:.2f}")
        self.perimeter_var.set(f"{perimeter:.2f}")


class Circle:
    def __init__(self, radius=0, diameter=0):
        if radius != 0:
            self.radius = radius
        elif diameter != 0:
            self.radius = diameter / 2
        else:
            self.radius = 0

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    CircleGUI()