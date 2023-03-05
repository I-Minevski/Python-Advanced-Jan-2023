guests = int(input())
invited = {input() for _ in range(guests)}
came = set()

while True:
    cmd = input()
    if cmd == "END":
        break
    else:
        came.add(cmd)

didnt_come = sorted(invited - came)
print(len(didnt_come))
print('\n'.join(didnt_come))