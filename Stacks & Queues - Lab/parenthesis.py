expression = input()
parenthesis = []

for i in range(len(expression)):
    if expression[i] == '(':
        parenthesis.append(i)
    elif expression[i] == ')':
        start_index = parenthesis.pop()
        print(expression[start_index:i + 1])
