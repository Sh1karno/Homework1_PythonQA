import pytest


class TestSetMethods:

    @pytest.mark.first_test_method
    @pytest.mark.passed_only
    def test_set_minus(self, create_set_one, create_set_two):
        assert create_set_two - create_set_one == \
               {'q', 'r', 't', 'w', 'y'}

    @pytest.mark.passed_only
    def test_set_union(self, create_set_one, create_set_two):
        assert create_set_one.union(create_set_two) == \
               create_set_one | create_set_two

    @pytest.mark.passed_only
    def test_set_intersection(self, create_set_one, create_set_two):
        assert create_set_one.intersection(create_set_two) == \
               create_set_one & create_set_two == {'e'}

    @pytest.mark.xfail(reason="One of the tests will fail as intended")
    @pytest.mark.parametrize("test_param", [{'a'}, {'n'}, {'m'}])
    def test_set_update(self, create_set_one, create_set_two, test_param):
        create_set_one.update(test_param)
        assert len(create_set_two) == len(create_set_one)

    @pytest.mark.passed_only
    def test_set_clear(self, create_set_one, create_set_two):
        create_set_one.clear()
        while create_set_two != set():
            create_set_two.pop()
        assert create_set_one == create_set_two
