from collections import deque

COMMAND_PAID = "Paid"
COMMAND_END = "End"

queue = deque()
while True:
    command = input()
    if command == COMMAND_END:
        print(f"{len(queue)} people remaining.")
        break
    elif command == COMMAND_PAID:
        while len(queue) > 0:
            print(queue.popleft())
    else:
        queue.append(command)