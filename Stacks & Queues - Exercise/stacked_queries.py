stack = []
n = int(input())

for i in range(n):
    command = input()
    if command.split(" ")[0] == "1":
        number = int(command.split(" ")[1])
        stack.append(number)
    elif command == "2":
        if len(stack) > 0:
            stack.pop()
    elif command == "3":
        if len(stack) > 0:
            print(max(stack))
    elif command == "4":
        if len(stack) > 0:
            print(min(stack))

print(", ".join(str(element) for element in reversed(stack)))