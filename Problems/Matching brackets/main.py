# put your python code here
from _collections import deque

bracket_stack = deque()

string = input()
try:
    for char in string:
        if char == "(":
            bracket_stack.append(char)
        elif char == ")":
            bracket_stack.pop()
    if len(bracket_stack) == 0:
        print("OK")
    else:
        print("ERROR")
except IndexError:
    print("ERROR")