number_of_user = int(input())

usernames = set()
for _ in range(number_of_user):
    user = input()
    usernames.add(user)

print(*usernames, sep='\n')