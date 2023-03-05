import os


def get_ext(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)
        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_level:
            get_ext(os.path.join(dir_name, filename), first_level=True)


directory = input()
extensions = {}

get_ext(directory)

with open(f"{directory}/report.txt", 'w') as file:
    for ext, files in sorted(extensions.items(), key=lambda x: (x[0], x[1])):
        file.write(f".{ext}\n")
        for file_name in files:
            file.write(f"- - - {file_name}\n")

