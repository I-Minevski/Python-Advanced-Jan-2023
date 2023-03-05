commands_count = int(input())
plate_records = [input() for _ in range(commands_count)]
CMD_IN = "IN"
CMD_OUT = "OUT"
parking_lot = set()

for record in plate_records:
    command, plate = record.split(", ")

    if command == CMD_IN:
        parking_lot.add(plate)
    elif command == CMD_OUT:
        parking_lot.remove(plate)

if len(parking_lot) > 0:
    print('\n'.join(parking_lot))
else:
    print("Parking Lot is Empty")

