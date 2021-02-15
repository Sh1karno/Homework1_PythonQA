import math

from Homework_to_lesson_OOP import shape_class


class ITriangle(shape_class.IShape):

    def __init__(self, side_one, side_two, angle=90, name='abc'):
        self.name = name
        self.angles = 3
        self.side_one = side_one
        self.side_two = side_two
        self.angle = angle
        self.side_three = self.get_side_three(self.side_one, self.side_two, self.angle)
        self.perimeter = self.get_perimeter(self.side_one, self.side_three, self.side_two)
        self.area = self.get_area(self.side_one, self.side_two, self.angle)

    @staticmethod
    def get_side_three(side_one, side_two, angle):
        side_three = math.sqrt(side_one**2 + side_two**2 - 2 * side_one * side_two * math.cos(math.radians(angle)))
        return side_three

    @staticmethod
    def get_perimeter(side_one, side_two, side_three):
        perimeter = side_one + side_two + side_three
        return perimeter

    @staticmethod
    def get_area(side_ab, side_ac, angle):
        area = 1/2 * side_ab * side_ac * math.sin(math.radians(angle))
        return area
