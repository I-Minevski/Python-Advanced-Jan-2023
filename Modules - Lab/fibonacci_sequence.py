from Fibonacci import *

sequence = []
while True:
    command = input().split(' ')

    if command[0] == 'Stop':
        break

    elif command[0] == 'Create':
        sequence = create_sequence(int(command[2]))
        print(*sequence, sep=' ')

    elif command[0] == 'Locate':
        locate(sequence, int(command[1]))