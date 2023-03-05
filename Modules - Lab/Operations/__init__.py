def calc(num1, operator, num2):

    num1 = float(num1)
    num2 = int(num2)

    def addition():
        return num1 + num2

    def multiplication():
        return num1 * num2

    def subtraction():
        return num1 - num2

    def division():
        return num1 / num2

    def raise_to_power():
        return num1 ** num2

    if operator == '+':
        return addition()
    elif operator == '*':
        return multiplication()
    elif operator == '-':
        return subtraction()
    elif operator == '/':
        return division()
    elif operator == '^':
        return raise_to_power()
