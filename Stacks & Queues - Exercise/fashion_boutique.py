clothes = [int(x) for x in input().split(" ")]
rack_capacity = int(input())
racks = 1
current_rack_capacity = rack_capacity

while len(clothes) > 0:
    if clothes[len(clothes)-1] <= current_rack_capacity:
        current_rack_capacity -= clothes.pop()
    else:
        racks += 1
        current_rack_capacity = rack_capacity
print(racks)
