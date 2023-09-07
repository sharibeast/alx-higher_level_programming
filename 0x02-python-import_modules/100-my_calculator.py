#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_of_args = len(sys.argv)

    if (number_of_args - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    not_add = operator != '+'
    if not_add and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import sub, div, mul, add

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '/':
        print("{} + {} = {}".format(a, b, div(a, b)))
    elif operator == '*':
        print("{} + {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} - {} = {}".format(a, b, sub(a, b)))
