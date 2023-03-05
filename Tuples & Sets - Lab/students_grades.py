students_count = int(input())
students = {}

for i in range(students_count):
    name, grade = info = input().split(" ")
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    average = sum(grades)/len(grades)
    grades_as_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    print(f"{name} -> {grades_as_string} (avg: {average})")
    #print(f"{name} -> {' '.join(map(lambda grade: f'{grade:.2f}', grades))} (avg: {sum(grades)/len(grades):.2f})") #top guzariq