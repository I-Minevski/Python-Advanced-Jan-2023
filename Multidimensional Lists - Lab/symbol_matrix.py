rows = int(input())
matrix = [[x for x in input().split(" ")] for j in range(rows)]
symbol = input()

for row in range(rows):
    string_on_row = matrix[row][0]
    for col in range(len(string_on_row)):
        if string_on_row[col] == symbol:
            print(f"({row}, {col})")
            raise SystemExit

print(f"{symbol} does not occur in the matrix")