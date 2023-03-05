rows, cols = (int(x) for x in input().split(", "))

matrix = []

for i in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

s = sum([sum(el) for el in matrix])
print(s)
print(matrix)