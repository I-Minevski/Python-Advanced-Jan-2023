def print_triangle(size):
    triangle = []
    for i in range(size):
        triangle.append([x for x in range(1, i + 2)])

    bottom_rows = []

    for row in reversed(triangle[:-1]):
        bottom_rows.append(row)

    triangle.extend(bottom_rows)

    for row in triangle:
        print(*row, sep=' ')