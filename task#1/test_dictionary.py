import pytest



class TestDictMethods:

    @pytest.mark.first_test_method
    @pytest.mark.passed_only
    def test_dict_copy(self, create_dict):
        copied_dict = create_dict.copy()
        assert copied_dict == create_dict

    @pytest.mark.passed_only
    @pytest.mark.parametrize("key, value", [(1, 1), (2, 4), (4, 16), (5, None)])
    def test_dict_get(self, create_dict, key, value):
        assert create_dict.get(key) == value

    @pytest.mark.passed_only
    @pytest.mark.xfail(reason="One of the tests will fail as intended")
    def test_dict_keys(self, create_dict):
        assert create_dict[4] in create_dict.keys()

    @pytest.mark.passed_only
    def test_dict_clear(self, create_dict):
        assert create_dict.clear() is None

    @pytest.mark.passed_only
    @pytest.mark.parametrize("key", [1, 2, 4])
    def test_dict_values(self, create_dict, key):
        value_dict = create_dict[key]
        assert value_dict in create_dict.values()




