import sys

def string_arg(string_input):

    rev = string_input[::-1].swapcase()
    return rev


if __name__ == "__main__":
    length = len(sys.argv)
    if (length > 1):
        i=1
        str=""
        while(length > 1):
            str += sys.argv[i] + " "
            i +=1
            length -=1
        result = string_arg(str)
        print(result)