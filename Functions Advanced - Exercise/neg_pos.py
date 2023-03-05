def sum_numbers(*args):
    pos = neg = 0
    for num in args:
        if num > 0:
            pos += num
        else:
            neg += num

    print(neg)
    print(pos)
    if abs(pos) > abs(neg):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


sum_numbers(*[int(x) for x in input().split()])