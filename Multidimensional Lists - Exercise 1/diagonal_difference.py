rows = int(input())
matrix = [[int(x) for x in input().split(" ")] for j in range(rows)]

primary = [matrix[i][i] for i in range(rows)]
secondary = [matrix[i][rows - 1 - i] for i in range(rows)]

print(abs(sum(primary) - sum(secondary)))