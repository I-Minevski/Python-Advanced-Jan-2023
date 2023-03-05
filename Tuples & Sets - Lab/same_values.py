values = tuple(map(float, input().split(" ")))
counter = {value: values.count(value) for value in values}
for k, v in counter.items():
    print(f"{k} - {v} times")