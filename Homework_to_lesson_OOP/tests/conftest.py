from datetime import datetime

import pytest

from .. import square_class
from .. import shape_class
from .. import rectangle_class
from .. import triangle_class
from .. import circle_class

@pytest.fixture(scope="session", autouse=True)
def set_time_testrun():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print('\nTEST-RUN RUNTIME:', end_time - start_time)


@pytest.fixture(scope="function", autouse=True)
def set_time_test():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(' | test-case runtime:', end_time - start_time)


@pytest.fixture
def create_shape_object():
    shape = shape_class.IShape('test shape', 5, 30, 40)
    return shape


@pytest.fixture
def create_square_object():
    square = square_class.ISquare(12)
    return square


@pytest.fixture
def create_rectangle_object():
    rectangle = rectangle_class.IRectangle(5, 10, 'ZXCV')
    return rectangle


@pytest.fixture
def create_triangle_object():
    triangle = triangle_class.ITriangle(4, 3, 45)
    return triangle


@pytest.fixture
def create_circle_object():
    circle = circle_class.ICircle(13, 'Test')
    return circle