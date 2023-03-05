from collections import deque

words = deque(input().split())

colors = {"red", "blue", "yellow", "orange", "purple", "green"}
secondary = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"}
}

keep = []

while words:
    first = words.popleft()
    last = words.pop() if words else ''

    for word in (first + last, last + first):
        if word in colors:
            keep.append(word)
            break
    else:
        for word in (first[:-1], last[:-1]):
            if word:
                words.insert(len(words) // 2, word)

for color in keep:
    if color in secondary.keys():
        if not secondary[color].issubset(keep):
            keep.remove(color)

print(keep)