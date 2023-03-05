from collections import deque

pumps_count = int(input())
pumps = deque([int(x) for x in input().split(" ")] for _ in range(pumps_count))
tank = 0
index = 0

total_distance = 0
for pump in pumps:
    total_distance += pump[1]

while True:
    run_distance = 0
    for pump in pumps:
        petrol, distance = pump[0], pump[1]
        if tank + petrol < distance:
            pumps.append(pumps.popleft())
            index += 1
            tank = 0
            break
        else:
            tank += (petrol - distance)
            run_distance += distance
    if run_distance == total_distance:
        break

print(index)