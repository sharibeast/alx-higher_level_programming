#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1

    if args == 0:
        print("{} arguments.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
    else:
        print("{} arguments:".format(args))

    if args >= 1:
        args = 0
        for i in sys.argv:
            if args != 0:
                print("{}: {}".format(args, i))
            args = args + 1
