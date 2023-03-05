from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split(" "))

print(max(orders))
while True:
    if orders[0] <= food_quantity:
        food_quantity -= orders[0]
        orders.popleft()
    else:
        break
    if len(orders) == 0:
        break


if len(orders) > 0:
    print(f"Orders left: {' '.join(str(order) for order in orders)}")
else:
    print("Orders complete")

