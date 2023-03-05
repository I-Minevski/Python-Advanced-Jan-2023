def grocery_store(**groceries):
    groceries = (sorted(groceries.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    result = []

    for k, v in groceries:
        result.append(f"{k}: {v}")

    return '\n'.join(result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

