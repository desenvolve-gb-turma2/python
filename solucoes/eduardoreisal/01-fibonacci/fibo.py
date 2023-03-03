#!/bin/python

class Fibonacci:
    """Fibonacci Class responsible for getting the n nums of Fibonacci sequence"""

    def __init__(self):
        """
        Initializer that will store the n nums of the Fibonacci sequence inside an array
        to make me able to access its values from anywhere
        """
        self.fibo_squence = []

    def calculate_fibo(self):
        """Function responsible for looping and getting the first n numbers of the Fibonacci sequence"""
        x, y = 0, 1
        while True:
            yield x
            x, y = y, x+y

    def get_fibo(self, num):
        fibo_squence_iterator = self.calculate_fibo()
        counter = 1
        print()
        while counter <= num:
            value = next(fibo_squence_iterator)
            self.fibo_squence.append(value)
            print(f"\033[34m\t\tSequence number: {counter} \t | \t Value {value}\033[31m")
            counter += 1
        print("")
        return self.fibo_squence

    def __str__(self):
        return f"{self.fibo_squence}"
