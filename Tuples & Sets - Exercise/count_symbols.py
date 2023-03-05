from collections import OrderedDict

values = tuple(input())
counter = {value: values.count(value) for value in values}
sorted_counter = OrderedDict(sorted(counter.items()))
for k, v in sorted_counter.items():
    print(f"{k}: {v} time/s")