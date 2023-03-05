from collections import deque

textiles = deque(int(x) for x in input().split(" "))
meds = [int(x) for x in input().split(" ")]

healing = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while meds and textiles:
    current_med = meds.pop()
    current_textile = textiles.popleft()
    sum_items = current_med + current_textile

    for key, value in healing.items():
        if sum_items == value:
            items[key] += 1
            break
    else:
        if sum_items > 100:
            items["MedKit"] += 1
            if meds:
                meds[-1] += (sum_items - 100)
            else:
                meds.append(sum_items - 100)
        else:
            meds.append(current_med + 10)


if not meds and not textiles:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not meds:
    print("Medicaments are empty.")

for key, value in sorted(items.items(), key=lambda x: (-x[1], x[0])):
    if value:
        print(f"{key} - {value}")

if meds:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(meds))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
