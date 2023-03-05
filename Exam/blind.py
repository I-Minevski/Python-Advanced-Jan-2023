rows, cols = (int(x) for x in input().split(" "))
matrix = [[x for x in input().split(" ")] for j in range(rows)]


def print_matrix():
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end='')
        print()


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

player_coordinates = []
caught = 0
moves = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 'B':
            matrix[i][j] = '-'
            player_coordinates = [i, j]


while True:
    command = input()

    if command == "Finish":
        break

    direction = directions[command]
    r = player_coordinates[0] + direction[0]
    c = player_coordinates[1] + direction[1]

    if 0 <= r < rows and 0 <= c < cols and matrix[r][c] != 'O':
        moves += 1
        if matrix[r][c] == 'P':
            caught += 1
            matrix[r][c] = '-'
        if caught == 3:
            break
        player_coordinates = [r, c]


print("Game over!")
print(f"Touched opponents: {caught} Moves made: {moves}")