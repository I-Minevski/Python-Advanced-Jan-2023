import os


def create_file(file_name):
    open(file_name, 'w')


def add_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(f"{content}\n")


def replace_in_file(file_name, old_string, new_string):
    try:

        with open(file_name, 'r') as file:
            text = file.readlines()

        for i in range(len(text)):
            text[i] = text[i].replace(old_string, new_string)

        with open(file_name, 'w') as file:
            file.write(''.join(text))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input().split('-')

    if command[0] == "End":
        break

    elif command[0] == "Create":
        create_file(command[1])

    elif command[0] == "Add":
        add_to_file(command[1], command[2])

    elif command[0] == "Replace":
        replace_in_file(command[1], command[2], command[3])

    elif command[0] == "Delete":
        delete_file(command[1])

