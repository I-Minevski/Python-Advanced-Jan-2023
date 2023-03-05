matrix = [[x for x in input().split(" ")] for j in range(5)]
n = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

targets = 0
targets_shot = 0
shot_coordinates = []

for i in range(5):
    targets += matrix[i].count('x')
    if 'A' in matrix[i]:
        player_position = [i, matrix[i].index('A')]

for i in range(n):
    command = input().split(' ')

    if command[0] == 'move':
        direction, steps = command[1], int(command[2])

        #for step in range(steps):
        r = player_position[0] + directions[direction][0] * steps
        c = player_position[1] + directions[direction][1] * steps

        if 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] != 'x':
                player_position[0], player_position[1] = r, c

    elif command[0] == 'shoot':
        direction = command[1]

        bullet_r = player_position[0] + directions[direction][0]
        bullet_c = player_position[1] + directions[direction][1]

        while 0 <= bullet_r < 5 and 0 <= bullet_c < 5:
            if matrix[bullet_r][bullet_c] == 'x':
                matrix[bullet_r][bullet_c] = '.'
                targets_shot += 1
                shot_coordinates.append([bullet_r, bullet_c])
                break

            bullet_r += directions[direction][0]
            bullet_c += directions[direction][1]

    if targets - targets_shot == 0:
        print(f"Training completed! All {targets} targets hit.")
        break

else:
    print(f"Training not completed! {targets - targets_shot} targets left.")

print(*shot_coordinates, sep='\n')

