def fill_the_box(height, length, width, *args):
    volume = height * width * length

    for el in args:
        if el != "Finish":
            cubes = int(el)
            if volume - cubes >= 0:
                volume -= cubes
            else:
                remaining = cubes - volume
                remaining += sum(args[args.index(el) + 1:-1])
                return f"No more free space! You have {remaining} more cubes."
        else:
            break

    return f"There is free space in the box. You could put {volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))