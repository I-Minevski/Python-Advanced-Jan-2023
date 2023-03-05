n, m = input().split(" ")
set1 = set()
set2 = set()

for i in range(int(n)):
    set1.add(input())

for i in range(int(m)):
    set2.add(input())

print('\n'.join(set1 & set2))