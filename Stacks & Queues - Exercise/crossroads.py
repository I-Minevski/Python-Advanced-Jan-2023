from collections import deque

CMD_GREEN = "green"
CMD_END = "END"

green_duration = int(input())
window = int(input())
cars = deque()
passed = 0

while True:
    command = input()

    if command == CMD_END:
        break
    elif command == CMD_GREEN:
        current_green = green_duration

        while current_green > 0 and cars:
            car = cars.popleft()

            current_window = current_green + window

            if len(car) > current_window:
                print(f"A crash happened!\n{car} was hit at {car[current_window]}.")
                raise SystemExit

            current_green -= len(car)
            passed += 1
    else:
        cars.append(command)

print(f"Everyone is safe.\n{passed} total cars passed the crossroads.")