def add_func(s, added):
    s.update([int(x) for x in added])


def remove_func(s, removed):
    for num in removed:
        s.discard(int(num))


seq1 = set(int(x) for x in input().split(" "))
seq2 = set(int(x) for x in input().split(" "))
n = int(input())

for i in range(n):
    command = input().split(" ")
    if "First" in command:
        if "Add" in command:
            add_func(seq1, command[2:])
        elif "Remove" in command:
            remove_func(seq1, command[2:])

    elif "Second" in command:
        if "Add" in command:
            add_func(seq2, command[2:])
        elif "Remove" in command:
            remove_func(seq2, command[2:])

    else:
        if seq1.issubset(seq2) or seq2.issubset(seq1):
            print(True)
        else:
            print(False)

print(*sorted(seq1), sep=', ')
print(*sorted(seq2), sep=', ')
