size = int(input())
board = [list(input()) for line in range(size)]

moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_pos = []

    for row in range(size):
        for col in range(size):
            if board[row][col] == 'K':
                attacks = 0

                for pos in moves:
                    move_row = row + pos[0]
                    move_col = col + pos[1]

                    if 0 <= move_row < size and 0 <= move_col < size:
                        if board[move_row][move_col] == 'K':
                            attacks += 1
                if max_attacks < attacks:
                    max_attacks = attacks
                    knight_pos = [row, col]

    if knight_pos:
        board[knight_pos[0]][knight_pos[1]] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)