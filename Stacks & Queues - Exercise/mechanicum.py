from collections import deque
from datetime import datetime, timedelta

servitors = {serv.split("-")[0]:[int(serv.split("-")[1]), 0] for serv in input().split(";")}
time = datetime.strptime(input(), "%H:%M:%S")

processable = deque()

while True:
    product = input()
    if product == "End":
        break
    else:
        processable.append(product)

while processable:
    time += timedelta(0, 1)
    product = processable.popleft()

    servitors = {serv[0]:[serv[1][0], serv[1][1] - 1] if serv[1][1] != 0 else serv[1] for serv in servitors.items()}
    idle_servitors = list(filter(lambda x: x[1][1] == 0, servitors.items()))

    if not idle_servitors:
        processable.append(product)
        continue
    else:
        servitors[idle_servitors[0][0]][1] = idle_servitors[0][1][0]
        print(f"{idle_servitors[0][0]} - {product} [{time.strftime('%H:%M:%S')}]")