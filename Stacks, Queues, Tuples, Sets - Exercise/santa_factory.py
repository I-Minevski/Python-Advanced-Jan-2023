from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
toys_made = []

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while magic and materials:
    current_material = materials.pop()
    current_magic = magic.popleft()

    level = current_magic * current_material
    if level in toys.keys():
        toys_made.append(toys[level])
    elif level < 0:
        materials.append(current_material + current_magic)
    elif level > 0:
        materials.append(current_material + 15)
    else:
        if current_material <= 0 and current_magic <= 0:
            continue
        elif current_material <= 0:
            magic.appendleft(current_magic)
            continue
        elif current_magic <= 0:
            materials.append(current_material)
            continue

if "Doll" in toys_made and "Wooden train" in toys_made:
    print("The presents are crafted! Merry Christmas!")

elif "Teddy bear" in toys_made and "Bicycle" in toys_made:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for value in sorted(toys.values()):
    if toys_made.count(value) > 0:
        print(f"{value}: {toys_made.count(value)}")