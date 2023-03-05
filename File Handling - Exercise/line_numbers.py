file_name = 'text.txt'

with open('text.txt') as file:
    lines = file.readlines()

output_file = 'output.txt'
open(output_file, 'w')

for i in range(len(lines)):
    count_alpha = 0
    count_punctuation = 0

    for word in lines[i].split():
        for char in word:
            if char.isalpha():
                count_alpha += 1
            elif not char.isalpha() and not char.isdigit():
                count_punctuation += 1

    with open(output_file, 'a') as file:
        file.write(f"Line {i+1}: {lines[i][:-1]} ({count_alpha})({count_punctuation})\n")