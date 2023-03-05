rows = int(input())

matrix = [[int(x) for x in input().split(" ")] for j in range(rows)]
coordinates = [[int(x) for x in coordinate.split(",")] for coordinate in input().split(" ")]

directions = (
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 1),
    (-1, -1),
    (1, -1),
    (1, 1),
    (0, 0)
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for i, j in directions:
        r, c = i + row, j + col

        if 0 <= r < rows and 0 <= c < rows and matrix[r][c] > 0:
            matrix[r][c] -= matrix[row][col]

alive = sum_alive = 0
for i in range(rows):
    for j in range(rows):
        if matrix[i][j] > 0:
            alive += 1
            sum_alive += matrix[i][j]

#alive_mtrx = [[x for x in line if x > 0]for line in matrix]
#alive = sum([len(x) for x in alive_mtrx])
#sum_alive = sum([sum(x) for x in alive_mtrx])

print(f"Alive cells: {alive}")
print(f"Sum: {sum_alive}")

for i in range(rows):
    for j in range(rows):
        print(matrix[i][j], end=' ')
    print()