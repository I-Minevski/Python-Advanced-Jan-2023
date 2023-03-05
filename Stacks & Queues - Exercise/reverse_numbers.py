numbers = input().split(" ")
reverse_stack = []

for i in range(len(numbers)):
    reverse_stack.append(numbers.pop())

print(" ".join(reverse_stack))