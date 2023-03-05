from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque(int(x) for x in input().split(", "))
shakes_made = 0

while shakes_made < 5 and milk and chocolate:
    current_milk = milk.popleft()
    current_chocolate = chocolate.pop()

    if current_milk <= 0 and current_chocolate <= 0:
        continue
    elif current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue
    elif current_milk <=0:
        chocolate.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        shakes_made += 1
    else:
        milk.append(current_milk)
        chocolate.append(current_chocolate - 5)

if shakes_made >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")