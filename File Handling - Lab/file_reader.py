def sum_numbers(file_name):
    data = open(file_name, 'r')
    sum_num = 0

    for numbers in data:
        sum_num += int(numbers)

    return sum_num


print(sum_numbers('text.txt'))