n = int(input())
intersections = []

for i in range(n):
    first_range, second_range = [x.split(",") for x in input().split("-")]

    set1 = set(range(int(first_range[0]), int(first_range[1]) + 1))
    set2 = set(range(int(second_range[0]), int(second_range[1]) + 1))

    intersections.append(set1 & set2)

intersections = list(sorted(intersections, key=lambda x: len(x), reverse=True))
print(f"Longest intersection is [{', '.join(str(x) for x in intersections[0])}] with length {len(intersections[0])}")
