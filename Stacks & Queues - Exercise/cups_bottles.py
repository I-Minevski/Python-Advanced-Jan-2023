from collections import deque

cups = deque(int(x) for x in input().split(" "))
bottles = [int(x) for x in input().split(" ")]

wasted = 0
cups_copy = cups.copy()

while cups:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted += current_bottle - current_cup
    else:
        cups.insert(0, current_cup)
        bottles[-1] += current_bottle

    if not bottles:
        print(f"Cups: {' '.join(str(x) for x in cups)}")
        print(f"Wasted litters of water: {wasted}")
        raise SystemExit

print(f"Bottles: {' '.join(str(x) for x in bottles)}")
print(f"Wasted litters of water: {wasted}")