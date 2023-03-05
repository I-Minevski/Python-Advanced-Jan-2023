rows, cols = (int(x) for x in input().split(" "))
matrix = [[x for x in input().split(" ")] for j in range(rows)]


def check_homogenous(lst):
    return all(el == lst[0] for el in lst)

    # return lst.count(lst[0]) == len(lst)
    # return len(set(lst)) == 1


homogenous_count = 0

for row in range(rows-1):
    for col in range(cols-1):
        square = [
            matrix[row][col],
            matrix[row][col+1],
            matrix[row+1][col],
            matrix[row+1][col+1]
        ]

        if check_homogenous(square):
            homogenous_count += 1

print(homogenous_count)