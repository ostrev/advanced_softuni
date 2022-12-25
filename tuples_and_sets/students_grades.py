number_of_students = int(input())
dic = {}

for _ in range(number_of_students):
    student, grade = tuple(input().split())
    grade = float(grade)
    if student not in dic:
        dic[student] = []
    dic[student].append(grade)

for key, value in dic.items():
    print(f'{key} -> {" ".join([f"{s:.2f}" for s in value])} (avg: {sum(value)/len(value):.2f})')


