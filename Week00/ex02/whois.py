import sys

def check_arg(arg):
    nbr = int(arg)
    if (nbr == 0):
        print("I'm Zero")
    elif (nbr % 2 == 0):
        print("I'm Odd")
    else:
        print("I'am Even")


if __name__ == "__main__":
    length = len(sys.argv)
    if (length > 2):
        print("AssertionError: more than one argument is provided")
    if (length == 2):
        if(not sys.argv[1].isdigit()):
            print("AssertionError: argument is not an integer")
        else:
            check_arg(sys.argv[1])