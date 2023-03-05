import sys

rows, cols = (int(x) for x in input().split(" "))
matrix = [[int(x) for x in input().split(" ")] for j in range(rows)]

max_sum = -sys.maxsize
max_square = []

for row in range(rows-2):
    for col in range(cols-2):
        square = [[matrix[row+i][col+j] for j in range(3)] for i in range(3)]

        current_sum = sum([sum(row) for row in square])
        if current_sum > max_sum:
            max_sum = current_sum
            max_square = square.copy()

print(f"Sum = {max_sum}")
for i in range(3):
    for j in range(3):
        print(max_square[i][j], end=' ')
    print()

