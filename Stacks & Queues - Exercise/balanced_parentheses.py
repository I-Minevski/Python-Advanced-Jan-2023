from collections import deque

parentheses = deque(input())
opening = deque()

while parentheses:
    leftmost = parentheses.popleft()
    if leftmost in "{[(":
        opening.append(leftmost)
    elif not opening:
        print("NO")
        break
    else:
        if f"{opening.pop() + leftmost}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")