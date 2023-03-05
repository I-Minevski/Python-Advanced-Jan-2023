size = int(input())
matrix = [[x for x in input().split(" ")] for j in range(size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'B':
            bunny_row, bunny_col = i, j

max_eggs = 0
max_dir = ""
best_path = []

for direction in directions.keys():
    eggs = 0

    r = bunny_row + directions[direction][0]
    c = bunny_col + directions[direction][1]

    eggs_pos = []

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == 'X':
            break
        else:
            eggs += int(matrix[r][c])
            eggs_pos.append([r, c])
            r += directions[direction][0]
            c += directions[direction][1]

    if eggs >= max_eggs:
        best_path = eggs_pos
        max_eggs = eggs
        max_dir = direction

print(max_dir)
print(*best_path, sep='\n')
print(max_eggs)