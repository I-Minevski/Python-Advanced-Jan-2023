from collections import deque
from functools import reduce

expression = deque(input().split(" "))
operators = {
    "*": lambda arr: reduce(lambda a, b: int(a) * int(b), arr),
    "+": lambda arr: reduce(lambda a, b: int(a) + int(b), arr),
    "-": lambda arr: reduce(lambda a, b: int(a) - int(b), arr),
    "/": lambda arr: reduce(lambda a, b: int(a) // int(b), arr)
}

while len(expression) > 1:
    current = []
    while str(expression[0]) not in "+-*/":
        current.append(expression.popleft())
    expression.insert(0, operators[expression.popleft()](current))

print(expression[0])