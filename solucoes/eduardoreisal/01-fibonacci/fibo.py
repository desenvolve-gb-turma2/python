#!/bin/python

class Fibonacci:
    """Fibonacci Class responsible for getting the n nums of Fibonacci sequence"""
    def __init__(self):
        """Initializer that will store the n nums of the Fibonacci sequence inside an array"""
        self.fibo_squence = []

    def get_fibo(self, num: int) -> int:
        """Recursive function responsible for getting n nums of Fibonacci sequence and storing it inside an array"""
        if num <= 1:
            return (num, 0)
        else:
            (x, z) = self.get_fibo(num - 1)
            self.fibo_squence.append(z)
            return (x + z, x)

    def __str__(self):
        return f"{self.fibo_squence}"
