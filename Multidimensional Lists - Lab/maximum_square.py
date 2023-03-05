rows, cols = (int(x) for x in input().split(", "))

matrix = [[int(x) for x in input().split(", ")] for j in range(rows)]

max_sum = 0
max_square = []

for row in range(rows-1):
    for col in range(cols-1):
        square = [
            matrix[row][col],
            matrix[row][col+1],
            matrix[row+1][col],
            matrix[row+1][col+1]
        ]

        if sum(square) > max_sum:
            max_sum = sum(square)
            max_square = square.copy()

for i in range(0, 3, 2):
    print(f"{max_square[i]} {max_square[i+1]}")
print(max_sum)