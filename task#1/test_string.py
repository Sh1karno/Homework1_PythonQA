import pytest



class TestStringMethod:

    @pytest.mark.first_test_method
    @pytest.mark.passed_only
    def test_string_len(self, create_string):
        assert len(create_string) == 5

    @pytest.mark.passed_only
    def test_string_isalpha(self, create_string):
        assert create_string.isalpha()

    @pytest.mark.passed_only
    def test_string_islower(self, create_string):
        assert create_string.islower()

    @pytest.mark.passed_only
    @pytest.mark.parametrize("half", [1, 2, 3, 4])
    def test_string_slice(self, create_string, half):
        first_half_string = create_string[:half]
        second_half_string = create_string[half:]
        assert first_half_string + second_half_string == create_string

    @pytest.mark.passed_only
    def test_string_title(self, create_string):
        assert create_string.title() == 'Abcde'