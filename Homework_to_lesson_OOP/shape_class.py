

class IShape:

    def __init__(self, name, angles, perimeter, area):
        self.name = name  # название фигуры
        self.angles = angles  # выводить количество углов
        self.perimeter = perimeter  # выводить периметр(суммудлинсторон, длинуокружности)
        self.area = area  # выводит площадь

    def add_area(self, shape):
        if isinstance(shape, IShape):
            area = self.area + shape.area
            return area
        else:
            return "ERROR: передан неправильный класс."
