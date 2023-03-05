from collections import deque

COMMAND_END = "End"
COMMAND_REFILL = "refill"

dispenser_capacity = int(input())
water_queue = deque()
while True:
    command = input()
    if command == "Start":
        break
    else:
        water_queue.append(command)
while True:
    command = input()
    if command == COMMAND_END:
        print(f"{dispenser_capacity} liters left")
        break
    elif command.startswith(COMMAND_REFILL):
        refilled = int(command.split(" ")[1])
        dispenser_capacity += refilled
    else:
        liters = int(command)
        person = water_queue.popleft()
        if liters <= dispenser_capacity:
            dispenser_capacity -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait" )