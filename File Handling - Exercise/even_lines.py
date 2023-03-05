file_name = 'text.txt'

with open('text.txt') as file:
    lines = file.readlines()

for i in range(len(lines)):
    if i % 2 == 0:
        line = list(reversed(lines[i].split()))

        for j in range(len(line)):
            edited = ""

            for k in line[j]:
                if k.isalpha():
                    edited += k
                else:
                    edited += '@'

            line[j] = edited

        print(' '.join(line))