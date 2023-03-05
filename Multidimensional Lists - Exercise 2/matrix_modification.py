rows = int(input())
matrix = [[int(x) for x in input().split(" ")] for j in range(rows)]

while True:
    command = input()
    if command == 'END':
        break

    com, row, col, value = command.split(" ")
    row, col, value = int(row), int(col), int(value)

    if not (row in range(0, rows) and col in range(0, rows)):
        print("Invalid coordinates")
        continue

    else:
        if com == 'Add':
            matrix[row][col] += value
        elif com == 'Subtract':
            matrix[row][col] -= value

for i in range(rows):
    for j in range(rows):
        print(matrix[i][j], end=' ')
    print()
