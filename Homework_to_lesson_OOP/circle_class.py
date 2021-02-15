import math

from Homework_to_lesson_OOP import shape_class


class ICircle(shape_class.IShape):

    def __init__(self, radius, name='a'):
        self.name = name
        self.angles = 0
        self.radius = radius
        self.diameter = self.radius * 2
        self.perimeter = self.get_perimeter(self.radius)
        self.area = self.get_area(self.radius)

    @staticmethod
    def get_perimeter(radius):
        perimeter = 2 * math.pi * radius
        return perimeter

    @staticmethod
    def get_area(radius):
        area = math.pi * (radius**2)
        return area
