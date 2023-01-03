num = int(input())

students = set()
for _ in range(num):
    line = input()
    students.add(line)

print('\n'. join(students))