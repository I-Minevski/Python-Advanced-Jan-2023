rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for j in range(rows)]

flattened = [x for submatrix in matrix for x in submatrix]
print(flattened)