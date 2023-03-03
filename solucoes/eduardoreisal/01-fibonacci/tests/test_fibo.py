from fibo import Fibonacci
import pytest

class TestClass:
    def test_when_receiving_10_returns_10_first_numbers_of_fibonacci_sequence(self):
        fibo = Fibonacci()
        result = fibo.get_fibo(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert result == expected
