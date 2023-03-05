def concatenate(*args, **kwargs):
    concatenated = ''.join(args)

    for key in kwargs.keys():
        concatenated = concatenated.replace(key, kwargs[key])

    return concatenated


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))