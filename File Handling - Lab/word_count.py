with open('words.txt') as file:
    words = file.read().split()

with open('text.txt') as file:
    text = []
    for i in range(3):
        line = file.readline().split()
        for j in range(len(line)):
            word = ""
            for ch in line[j]:
                if ch.isalpha():
                    word += ch.lower()
            line[j] = word
        text.append(line)

word_counter = {}

for word in words:
    if word not in word_counter.keys():
        word_counter[word] = 0
    for line in text:
        word_counter[word] += line.count(word)

for k, v in sorted(word_counter.items(), key=lambda x: -x[1]):
    print(f"{k} - {v}")