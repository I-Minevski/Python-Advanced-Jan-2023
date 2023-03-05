rows = int(input())
commands = input().split(" ")
matrix = [[x for x in input().split(" ")] for j in range(rows)]

miner_row = miner_col = 0
total_coal = 0
collected_coal = 0

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == 's':
            miner_row, miner_col = i, j
            break

        if matrix[i][j] == 'c':
            total_coal += 1

for command in commands:

    if command == 'up' and miner_row > 0:
        miner_row -= 1
    elif command == 'down' and miner_row < rows - 1:
        miner_row += 1
    elif command == 'left' and miner_col > 0:
        miner_col -= 1
    elif command == 'right' and miner_col < rows - 1:
        miner_col += 1

    if matrix[miner_row][miner_col] == 'e':
        print(f"Game over! ({miner_row}, {miner_col})")
        raise SystemExit

    if matrix[miner_row][miner_col] == 'c':
        collected_coal += 1
        matrix[miner_row][miner_col] = '*'

    if collected_coal == total_coal:
        print(f"You collected all coal! ({miner_row}, {miner_col})")
        raise SystemExit

if collected_coal < total_coal:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_row}, {miner_col})")