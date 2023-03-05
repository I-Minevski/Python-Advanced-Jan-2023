from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = 0

operators = {
    "*": lambda a, b: a*b,
    "+": lambda a, b: a+b,
    "-": lambda a, b: a-b,
    "/": lambda a, b: a/b
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        if current_nectar == 0 and symbols[0] == '/':
            continue
        honey += abs(operators[symbols.popleft()](current_bee, current_nectar))
    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")