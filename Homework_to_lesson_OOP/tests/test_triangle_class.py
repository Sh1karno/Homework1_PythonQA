import pytest


@pytest.mark.triangle
class TestTriangleClass:

    def test_triangle_default_name(self, create_triangle_object):
        assert create_triangle_object.name == 'abc'

    def test_triangle_count_angles(self, create_triangle_object):
        assert create_triangle_object.angles == 3

    def test_triangle_calculate_side_three(self, create_triangle_object):
        assert create_triangle_object.side_three == create_triangle_object.get_side_three(4, 3, 45) == \
            2.833626166508712

    def test_triangle_calculate_perimeter(self, create_triangle_object):
        assert create_triangle_object.perimeter == \
            create_triangle_object.side_one + create_triangle_object.side_two + create_triangle_object.side_three == \
            9.833626166508711

    def test_triangle_calculate_area(self, create_triangle_object):
        assert create_triangle_object.area == create_triangle_object.get_area(4, 3, 45) == \
               4.242640687119285
