"""
This is used when there are many classes with implementation differences. One is implementation dependant like
AreaCalculator
Another one is implementation independant. like Shape.

The bridge pattern tries to simplify the hierarchy
"""


class AreaCalculator1:
    def __init__(self):
        self.name = "RECTANGLE"

    def area(self, length, breadth, radius):
        return "Object {2} -->  AREA = length * breadth = {0} * {1}".format(length, breadth, self.name)


class AreaCalculator2:
    def __init__(self):
        self.name = "CIRCLE"

    def area(self, length, breadth, radius):
        return "Object {1} --> AREA = 3.142 * radius * radius  = 3.142 * {0} * {0}".format(radius, self.name)


class Shape:
    def __init__(self, length, breadth, radius, area_obj):
        self.length = length
        self.breadth = breadth
        self.radius = radius
        self.area_calculator = area_obj

    def calculate_area(self):
        print(self.area_calculator.area(self.length, self.breadth, self.radius))


circle = Shape(0, 0, 3.5, AreaCalculator2())
circle.calculate_area()

rectangle = Shape(10, 30, 0, AreaCalculator1())
rectangle.calculate_area()

