import string
import sys

def text_analyzer(text=None):
    """
    This function counts the number of printable characters,
    upper-case letters, lower-case letters, punctuation marks,
    and spaces in the given text.
    If no text is provided, it prompts the user for input.
    Raises an AssertionError if the argument is not a string.
    """
    if not text:
        text = input("what is the text to analyze?\n>> ")

    assert isinstance(text, str), "argument is not a string"
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    printable = 0
    for c in text:
        if c.isprintable():
            printable +=1
        if c.isupper():
            upper +=1
        if c.islower():
            lower +=1
        if c == " " :
            spaces +=1
        if c in string.punctuation:
            punctuation +=1
    print(f"The text contains {printable} printable character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {spaces} space(s)")


if __name__ == "__main__":
    if (len(sys.argv) > 2):
        print("error: too many arguments")
    elif(len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()