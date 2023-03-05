compounds = int(input())
elements = set()

for i in range(compounds):
    elements.update(input().split(" "))

print('\n'.join(elements))