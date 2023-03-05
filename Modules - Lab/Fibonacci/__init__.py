def fibonacci(n):
    if n in (0, 1):
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def create_sequence(count):
    return [fibonacci(x) for x in range(count)]


def locate(seq, number):
    if number in seq:
        print(f"The number - {number} is at index {seq.index(number)}")
    else:
        print(f"The number {number} is not in the sequence")
