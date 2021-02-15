import pytest


@pytest.mark.shape
class TestShapeClass:

    def test_shape_assigned_name(self, create_shape_object):
        assert create_shape_object.name == 'test shape'

    def test_shape_angles(self, create_shape_object):
        assert create_shape_object.angles == 5

    def test_shape_perimeter(self, create_shape_object):
        assert create_shape_object.perimeter == 30

    def test_shape_area(self, create_shape_object):
        assert create_shape_object.area == 40

    def test_shape_method(self, create_shape_object):
        assert create_shape_object.add_area(create_shape_object) == \
               create_shape_object.area * 2 == 80

    def test_shape_method_fail(self, create_shape_object):
        some_area = 30
        assert create_shape_object.add_area(some_area) == \
            "ERROR: передан неправильный класс."
