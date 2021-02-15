from Homework_to_lesson_OOP import shape_class


class IRectangle(shape_class.IShape):

    def __init__(self, side_one, side_two, name='abcd'):
        self.name = name
        self.angles = 4
        self.side_one = side_one
        self.side_two = side_two
        self.perimeter = self.get_perimeter(self.side_one, self.side_two)
        self.area = self.get_area(self.side_one, self.side_two)

    @staticmethod
    def get_perimeter(side_one, side_two):
        perimeter = 2 * (side_one + side_two)
        return perimeter

    @staticmethod
    def get_area(side_one, side_two):
        area = side_one * side_two
        return area
