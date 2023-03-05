def age_assignment(*names, **age_info):
    final_info = {}

    for letter, age in age_info.items():
        for name in names:
            if name[0] == letter:
                final_info[name] = age

    #return '\n'.join([f"{name} is {age} years old." for name, age in sorted(final_info.items(), key=lambda x: x[0])])

    result = []
    for name, age in sorted(final_info.items(), key=lambda x: x[0]):
        result.append(f"{name} is {age} years old.")

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))