def sorting_cheeses(**kwargs):
    result = []
    for (name, quantities) in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(name)
        result.extend(list(sorted(quantities, reverse=True)))

    return '\n'.join(str(x) for x in result)


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
