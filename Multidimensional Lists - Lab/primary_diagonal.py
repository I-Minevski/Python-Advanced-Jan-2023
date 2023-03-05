rows = int(input())
matrix = [[int(x) for x in input().split(" ")] for j in range(rows)]

print(sum([matrix[i][i] for i in range(rows)]))