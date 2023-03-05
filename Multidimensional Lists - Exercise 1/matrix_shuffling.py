def swap_elements(mtrx, com):
    com_list = com.split(" ")
    if len(com_list) != 5:
        print("Invalid input!")
    else:
        keyword = com_list[0]
        com_list = [int(coord) for coord in com_list[1:]]
        row1, col1, row2, col2 = com_list

        if keyword != 'swap' or any(coord < 0 for coord in com_list):
            print("Invalid input!")
        elif row1 > len(mtrx) or row2 > len(mtrx):
            print("Invalid input!")
        else:
            mtrx[row1][col1], mtrx[row2][col2] = mtrx[row2][col2], mtrx[row1][col1]
            for i in range(len(mtrx)):
                for j in range(len(mtrx[i])):
                    print(matrix[i][j], end=' ')
                print()


rows, cols = (int(x) for x in input().split(" "))
matrix = [[x for x in input().split(" ")] for j in range(rows)]

while True:
    command = input()

    if command == "END":
        break

    else:
        swap_elements(matrix, command)