from math import log


def logarithm(num, base):
    if base == 'natural':
        return log(num)
    else:
        return log(num, float(base))


number = int(input())
base = input()

print(f"{logarithm(number, base):.2f}")
