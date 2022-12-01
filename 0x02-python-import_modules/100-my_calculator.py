#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

num = len(sys.argv)
operator = ['+', '-', '*', '/']

if __name__ == "__main__":
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        oper = sys.argv[2]
        a = sys.argv[1]
        b = sys.argv[3]
        if operator[0] == oper:
            print(f"{a} + {b} = {add(int(a), int(b))}")
        elif operator[1] == oper:
            print(f"{a} - {b} = {sub(int(a), int(b))}")
        elif operator[2] == oper:
            print(f"{a} * {b} = {mul(int(a), int(b))}")
        elif operator[3] == oper:
            print(f"{a} / {b} = {div(int(a), int(b))}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
