from Homework_to_lesson_OOP import shape_class


class ISquare(shape_class.IShape):

    def __init__(self, side, name='abcd'):
        self.name = name
        self.angles = 4
        self.side = side
        self.perimeter = self.get_perimeter(self.side)
        self.area = self.get_area(self.side)

    @staticmethod
    def get_perimeter(side):
        perimeter = side * 4
        return perimeter

    @staticmethod
    def get_area(side):
        area = side ** 2
        return area
