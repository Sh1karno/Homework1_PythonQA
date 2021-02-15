import pytest


@pytest.mark.rectangle
class TestRectangleClass:

    def test_rectangle_assigned_name(self, create_rectangle_object):
        assert create_rectangle_object.name == 'ZXCV'

    def test_rectangle_count_angles(self, create_rectangle_object):
        assert create_rectangle_object.angles == 4

    def test_rectangle_calculate_perimeter(self, create_rectangle_object):
        assert create_rectangle_object.perimeter == \
               create_rectangle_object.get_perimeter(10, 5) == 30

    def test_rectangle_calculate_area(self, create_rectangle_object):
        assert create_rectangle_object.area == \
            create_rectangle_object.side_one * create_rectangle_object.side_two == 50

    def test_rectangle_add_area_method(self, create_rectangle_object, create_shape_object):
        assert create_rectangle_object.add_area(create_shape_object) == \
            create_rectangle_object.area + create_shape_object.area == 90
