presents = int(input())
size = int(input())
matrix = [[x for x in input().split(" ")] for j in range(size)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

nice = 0
happy = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 'S':
            santa_row, santa_col = i, j
            matrix[i][j] = '-'

        if matrix[i][j] == 'V':
            nice += 1

while True:
    if presents <= 0:
        if nice != happy:
            print("Santa ran out of presents!")
        break

    command = input()

    if command == "Christmas morning":
        break

    direction = directions[command]
    santa_row += direction[0]
    santa_col += direction[1]

    if 0 <= santa_row < size and 0 <= santa_col < size:
        if matrix[santa_row][santa_col] == 'V':
            presents -= 1
            happy += 1

        elif matrix[santa_row][santa_col] == 'C':
            for d in directions.keys():
                r, c = santa_row + directions[d][0], santa_col + directions[d][1]

                if matrix[r][c] == 'V':
                    matrix[r][c] = '-'
                    presents -= 1
                    happy += 1

                if matrix[r][c] == 'X':
                    matrix[r][c] = '-'
                    presents -= 1

                if presents <= 0:
                    break

        matrix[santa_row][santa_col] = '-'

matrix[santa_row][santa_col] = 'S'

for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=' ')
    print()

if happy == nice:
    print(f"Good job, Santa! {nice} happy nice kid/s.")
else:
    print(f"No presents for {nice - happy} nice kid/s.")
