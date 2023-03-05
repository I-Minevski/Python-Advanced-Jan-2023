rows, cols = (int(x) for x in input().split(", "))

matrix = [[int(x) for x in input().split(" ")] for j in range(rows)]

for j in range(cols):
    sum_column = 0
    for i in range(rows):
        sum_column += matrix[i][j]
    print(sum_column)