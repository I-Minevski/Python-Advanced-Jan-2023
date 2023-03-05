from collections import deque

kids = input()
potato_queue = deque(kids.split(" "))
step = int(input())
counter = 0

while len(potato_queue) > 1:
    counter += 1
    current_kid = potato_queue.popleft()
    if counter == step:
        print(f"Removed {current_kid}")
        counter = 0
    else:
        potato_queue.append(current_kid)
print(f"Last is {potato_queue.popleft()}")