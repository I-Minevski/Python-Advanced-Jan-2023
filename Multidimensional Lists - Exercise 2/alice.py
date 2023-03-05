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
        if matrix[i][j] == 'A':
            alice_row, alice_col = i, j
            matrix[i][j] = '*'
            break

teabags = 0

while True:
    command = input()
    direction = directions[command]
    alice_row += direction[0]
    alice_col += direction[1]

    if not (0 <= alice_row < size and 0 <= alice_col < size):
        print("Alice didn't make it to the tea party.")
        break

    field_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = '*'

    if field_value == 'R':
        print("Alice didn't make it to the tea party.")
        break

    else:
        if field_value.isdigit():
            teabags += int(field_value  )
            if teabags >= 10:
                print("She did it! She went to the party.")
                break

for i in range(size):
    print(' '.join(matrix[i]))
