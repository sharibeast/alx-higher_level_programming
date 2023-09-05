#!/usr/bin/python3
for number in range(0, 10):
    for m in range(number+1, 10):
        if (not (n == 8 and m == 9)):
            print("{}{}".format(n, m), end=",")
        else:
            print("{}{}".format(number, m))
