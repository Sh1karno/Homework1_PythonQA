import pytest


@pytest.mark.square
class TestSquareClass:

    def test_square_default_name(self, create_square_object):
        assert create_square_object.name == 'abcd'

    def test_square_side(self, create_square_object):
        assert create_square_object.side == 12

    def test_calculate_square_perimeter(self, create_square_object):
        assert create_square_object.perimeter == 48

    def test_calculate_square_area(self, create_square_object):
        assert create_square_object.area == 144

    def test_add_area_method_with_square_class(self, create_shape_object, create_square_object):
        assert create_square_object.add_area(create_shape_object) == \
            create_square_object.area + create_shape_object.area == 184
