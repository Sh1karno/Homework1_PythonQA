import pytest
from datetime import datetime


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
def create_list():
    list_data = [i for i in range(1, 5)]
    return list_data


@pytest.fixture
def create_string():
    string_data = 'abcde'
    return string_data


@pytest.fixture
def create_set_one(create_string):
    set_data_one = set(create_string)
    return set_data_one


@pytest.fixture
def create_set_two():
    set_data_two = set('qwerty')
    return set_data_two


@pytest.fixture
def create_dict(create_list):
    dict_data = {i: i ** 2 for i in create_list}
    return dict_data
