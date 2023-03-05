string = list(input())
reverse_stack = []

for i in range(len(string)):
    reverse_stack.append(string.pop())

print("".join(reverse_stack))