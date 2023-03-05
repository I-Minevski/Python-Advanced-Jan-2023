names_count = int(input())
counter = 1
set_even = set()
set_odd = set()

for i in range(names_count):
    name = list(input())
    power = sum(list(map(lambda x: ord(x), name)))//counter
    if power % 2 == 0:
        set_even.add(power)
    else:
        set_odd.add(power)
    counter += 1

sum_even = sum(set_even)
sum_odd = sum(set_odd)

if sum_odd == sum_even:
    print(', '.join(str(x) for x in list(set_odd.union(set_even))))  # set_odd|set_even
elif sum_odd > sum_even:
    print(', '.join(str(x) for x in list(set_odd.difference(set_even))))  # set_odd-set_even
else:
    print(', '.join(str(x) for x in list(set_odd.symmetric_difference(set_even))))  # set_odd^set_even
