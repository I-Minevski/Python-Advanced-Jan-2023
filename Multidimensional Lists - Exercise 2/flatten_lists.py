numbers = [[x for x in el.split()] for el in input().split("|")]

for i in range(len(numbers)-1, -1, -1):
    for num in numbers[i]:
        print(num, end=' ')
