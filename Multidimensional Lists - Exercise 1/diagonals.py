rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for j in range(rows)]

primary = [matrix[i][i] for i in range(rows)]
secondary = [matrix[i][rows - 1 - i] for i in range(rows)]

print(f"""Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}
Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}"""
)