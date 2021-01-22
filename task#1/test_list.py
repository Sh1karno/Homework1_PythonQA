import pytest



class TestListMethods:

    @pytest.mark.first_test_method
    @pytest.mark.passed_only
    def test_list_index(self, create_list):
        assert create_list.index(2) == 1

    @pytest.mark.passed_only
    def test_list_append(self, create_list):
        create_list.append([22, 55])
        assert create_list == [1, 2, 3, 4, [22, 55]]

    @pytest.mark.xfail(reason="Knowingly false test")
    def test_list_extend(self, create_list):
        create_list.extend([22, 55])
        assert create_list == [1, 2, 3, 4, [22, 55]]

    @pytest.mark.passed_only
    def test_list_insert(self, create_list):
        create_list.insert(2, 99)
        assert create_list == [1, 2, 99, 3, 4]

    @pytest.mark.parametrize("test_param, test_index", [(99, 3), (99, 2), (99, 1)])
    def test_list_count(self, create_list, test_param, test_index):
        create_list.insert(test_index, test_param)
        create_list.append(test_param)
        assert create_list.count(test_param) == 2
