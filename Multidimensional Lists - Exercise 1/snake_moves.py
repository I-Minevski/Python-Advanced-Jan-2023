rows, cols = (int(x) for x in input().split(" "))
string = list(input())

index = 0
matrix = []

for i in range(rows):
    line = []
    if i % 2 == 0:
        for j in range(cols):
            line.append(string[index])
            if index < len(string) - 1:
                index += 1
            else:
                index = 0

    else:
        for j in range(cols - 1, -1, -1):
            line.append(string[index])
            if index < len(string) - 1:
                index += 1
            else:
                index = 0
    matrix.append(line)

for i in range(rows):
    if i % 2 == 0:
        for j in range(cols):
            print(matrix[i][j], end='')
    else:
        for j in range(cols - 1, -1, -1):
            print(matrix[i][j], end='')
    print()
