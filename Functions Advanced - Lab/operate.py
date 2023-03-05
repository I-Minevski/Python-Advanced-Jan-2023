def operate(operator, *args):

    def addition():
        result = args[0]
        for num in args[1:]:
            result += num
        return result

    def multiplication():
        result = args[0]
        for num in args[1:]:
            result *= num
        return result

    def subtraction():
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def division():
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    if operator == '+':
        return addition()
    elif operator == '*':
        return multiplication()
    elif operator == '-':
        return subtraction()
    elif operator == '/':
        return division()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
