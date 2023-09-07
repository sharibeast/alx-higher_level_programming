#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = len(sys.argv)
    sum = 0
    for n in range(arguments - 1):
        sum = sum + int(sys.argv[n + 1])
    print("{}".format(sum))

