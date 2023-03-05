name_count = int(input())
usernames =[]

for i in range(name_count):
    usernames.append(input())

usernames_set = {name for name in usernames}
print('\n'.join(usernames_set))