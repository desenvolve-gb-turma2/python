#!/bin/python
from fibo import Fibonacci
import argparse


class Main:
    """Main class responsible for the logic of my program."""

    def __init__(self):
        """Instantiate my parser to make me able to call it from anywhere inside main """
        self.parser = argparse.ArgumentParser(
            description='Get first n nums from Fibonacci sequence')
        self.parser.add_argument(
            '--num', help='python main.py --num 10 | get first 10 nums from Fibonacci sequence')

    def validate_user_input_int(self, value) -> int:
        """Validate user input and keeps asking for new input until the user give the correct input"""
        try:
            value = int(value)
            return value
        except:
            print('[-] You need to enter a number')
            value = input(
                'How many of the n nums from Fibonacci sequence would you like to get: ')
            return self.validate_user_input_int(value)

    def get_user_input(self) -> int:
        """Ask for input and submit it to validation"""
        args = self.parser.parse_args()
        num = self.validate_user_input_int(args.num)
        return num


def main_func():
    """Main function responsible for putting together all classes and logic"""
    if __name__ == '__main__':
        starter = Main()
        num = starter.get_user_input()
        fibo = Fibonacci()
        fibo.get_fibo(num)


main_func()
