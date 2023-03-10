from main import Main 
import pytest

class Test:
    def test_when_receive_valid_number_return_it(self):
        starter = Main()
        result = starter.validate_user_input_int(10)
        expected = 10
        assert result == expected

