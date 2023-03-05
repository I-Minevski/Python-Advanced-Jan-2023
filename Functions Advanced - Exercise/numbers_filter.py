def even_odd_filter(**kwargs):
    filtered = {}

    for k, v in kwargs.items():
        if k == 'odd':
            filtered[k] = list(filter(lambda x: x % 2 != 0, v))
        else:
            filtered[k] = list(filter(lambda x: x % 2 == 0, v))

    sort_filtered = sorted(filtered.items(), key=lambda x: -len(x[1]))
    filtered = {k:v for k, v in sort_filtered}
    return filtered


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
