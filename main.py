# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
           opening_brackets_stack.append(Bracket(next,i+1))
           pass
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
            pass


def main():
    print("input - F or I")
    select_input = input()
    if select_input.upper() == "F":
        file_path = input("choose file (input path)")
        with open(file_path, "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            if mismatch == None:
                print("Success")
            else:
                print(mismatch)
    elif select_input.upper() == "I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == None:
            print("Success")
        else:
            print(mismatch)


if __name__ == "__main__":
    main()