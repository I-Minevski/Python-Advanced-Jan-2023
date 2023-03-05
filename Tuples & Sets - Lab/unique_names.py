name_count = int(input())
names =[]

for i in range(name_count):
    names.append(input())

names_set = {name for name in names}
print('\n'.join(names_set))