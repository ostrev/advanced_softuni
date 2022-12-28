number_of_students = int(input())
students = {}
for _ in range(number_of_students):
    data = input().split()
    name = data[0]
    grade = float(data[1])

    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    print(f"{student} -> {' '.join([f'{s:.2f}' for s in grades])} (avg: {sum(grades)/len(grades):.2f})")