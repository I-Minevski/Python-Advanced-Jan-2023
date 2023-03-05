def math_operations(*numbers, **operations):
    for i in range(len(numbers)):
        key = list(operations.keys())[i % 4]
        try:
            if key == 'a':
                operations[key] += numbers[i]
            elif key == 's':
                operations[key] -= numbers[i]
            elif key == 'd':
                operations[key] /= numbers[i]
            elif key == 'm':
                operations[key] *= numbers[i]
        except ZeroDivisionError:
            continue

    operations = sorted(operations.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join(f"{op}: {value:.1f}" for op, value in operations)




print(math_operations(6.0, a=0, s=0, d=5, m=0))