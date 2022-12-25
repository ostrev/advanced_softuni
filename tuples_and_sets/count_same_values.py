numbs = tuple(float(el) for el in input().split())
dic = {}

for num in numbs:
    if num not in dic:
        dic[num] = 0
    dic[num] += 1
for key, value in dic.items():
    print(f'{key} - {value} times')