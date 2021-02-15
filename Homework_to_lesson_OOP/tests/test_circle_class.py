import pytest


@pytest.mark.circle
class TestCircleClass:

    def test_circle_assigned_name(self, create_circle_object):
        assert create_circle_object.name == 'Test'

    def test_circle_radius(self, create_circle_object):
        assert create_circle_object.radius == 13

    def test_circle_diameter(self, create_circle_object):
        assert create_circle_object.diameter == create_circle_object.radius * 2 == 26

    def test_circle_calculate_perimeter(self, create_circle_object):
        assert create_circle_object.perimeter == create_circle_object.get_perimeter(13) == \
               81.68140899333463

    def test_circle_calculate_area(self, create_circle_object):
        assert create_circle_object.area == create_circle_object.get_area(13) == \
               530.929158456675

    def test_circle_add_area_method(self, create_circle_object, create_shape_object):
        assert create_circle_object.add_area(create_shape_object) == \
            create_circle_object.area + create_shape_object.area == \
               570.929158456675
