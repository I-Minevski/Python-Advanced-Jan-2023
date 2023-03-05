rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for j in range(rows)]

even = [[x for x in matrix[j] if x % 2 == 0] for j in range(rows)]
print(even)
