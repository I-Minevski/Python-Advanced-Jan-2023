rows, cols = (int(x) for x in input().split(" "))

matrix = []

for i in range(rows):
    line = []
    first = third = chr(ord('a') + i)
    for j in range(cols):
        second = chr(ord('a') + i + j)
        palindrome = first + second + third
        line.append(palindrome)
    matrix.append(line)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()