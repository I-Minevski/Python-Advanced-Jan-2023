def create_matrix(rows: int, columns: int):
    matrix = []

    for _ in range(rows):
        matrix.append([0] * columns)

    # Same logic using comprehension -> less readable
    # matrix = [[0] * columns for _ in range(rows)]

    return matrix


def player_choice(player):
    choice = input(f"Player {player}, please choose a column:\n")

    return int(choice) - 1


def main_logic(playground, player_index, player):
    start_row_index = 0

    while start_row_index < len(playground) and playground[start_row_index][player_index] == 0:
        start_row_index += 1

    playground[start_row_index - 1][player_index] = player

    return start_row_index - 1, player_index


def check_win_conditions(playground, row_index, col_index, win_counter):
    def right_win_condition(playground, row_index, col_index, max_col_index):
        right_values = [playground[row_index][i] for i in range(col_index, max_col_index)]
        return right_values

    def left_win_condition(playground, row_index, col_index, min_col_index):
        left_values = [playground[row_index][i] for i in range(col_index, min_col_index, -1)]
        return left_values

    def up_win_condition(playground, row_index, col_index, min_row_index):
        up_values = [playground[i][col_index] for i in range(row_index, min_row_index, -1)]
        return up_values

    def down_win_condition(playground, row_index, col_index, max_row_index):
        down_values = [playground[i][col_index] for i in range(row_index, max_row_index)]
        return down_values

    def down_right_win_condition(playground, row_index, col_index, max_row_index, max_col_index):
        diagonal_index = min(max_row_index - row_index, max_col_index - col_index)
        down_right_values = [playground[row_index + i][col_index + i] for i in range(diagonal_index)]
        return down_right_values

    def down_left_win_condition(playground, row_index, col_index, max_row_index, min_col_index):
        diagonal_index = min(max_row_index - row_index, abs(min_col_index - col_index))
        down_left_values = [playground[row_index + i][col_index - i] for i in range(diagonal_index)]
        return down_left_values

    def up_right_win_condition(playground, row_index, col_index, min_row_index, max_col_index):
        diagonal_index = min(abs(min_row_index - row_index), max_col_index - col_index)
        up_right_values = [playground[row_index - i][col_index + i] for i in range(diagonal_index)]
        return up_right_values

    def up_left_win_condition(playground, row_index, col_index, min_row_index, min_col_index):
        diagonal_index = min(abs(min_row_index - row_index), abs(min_col_index - col_index))
        up_left_values = [playground[row_index - i][col_index - i] for i in range(diagonal_index)]
        return up_left_values

    max_col_index = min(col_index + win_counter, len(playground[row_index]))
    min_col_index = max(-1, col_index - win_counter)
    max_row_index = min(row_index + win_counter, len(playground))
    min_row_index = max(-1, row_index - win_counter)

    right_win_values = right_win_condition(playground, row_index, col_index, max_col_index)
    left_win_values = left_win_condition(playground, row_index, col_index, min_col_index)
    up_win_values = up_win_condition(playground, row_index, col_index, min_row_index)
    down_win_values = down_win_condition(playground, row_index, col_index, max_row_index)

    down_right_win_values = down_right_win_condition(playground, row_index, col_index, max_row_index, max_col_index)
    down_left_win_values = down_left_win_condition(playground, row_index, col_index, max_row_index, min_col_index)
    up_right_win_values = up_right_win_condition(playground, row_index, col_index, min_row_index, max_col_index)
    up_left_win_values = up_left_win_condition(playground, row_index, col_index, min_row_index, min_col_index)

    possible_winner = [
        right_win_values,
        left_win_values,
        up_win_values,
        down_win_values,
        down_left_win_values,
        down_right_win_values,
        up_left_win_values,
        up_right_win_values
    ]

    return any(len(current_list) == win_counter and len(set(current_list)) == 1 for current_list in possible_winner)

    #for current_list in possible_winner:
     #   if len(current_list) == win_counter and len(set(current_list)) == 1:
      #      return True
    #return False


def gameplay_function(playground, win_counter):
    current_player, second_player = 1, 2

    while True:
        try:
            current_player_choice = player_choice(current_player)

            row_index, col_index = main_logic(playground, current_player_choice, current_player)

            print_function(playground)

            if check_win_conditions(playground, row_index, col_index, win_counter):
                print(f"The winner is Player {current_player}")
                break

            current_player, second_player = second_player, current_player
        except IndexError:
            print("Invalid column. Try again!")


def print_function(playground):
    for row in playground:
        print(row)


try:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    win_counter = int(input("Enter the win combination:  "))
    playground = create_matrix(rows, columns)
    gameplay_function(playground, 4)
except ValueError:
    print("Invalid values. Try again!")