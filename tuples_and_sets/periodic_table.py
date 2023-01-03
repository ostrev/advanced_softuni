count = int(input())

elements_set = set()
for _ in range(count):
    line = input().split()
    for el in line:
        elements_set.add(el)

print(*elements_set, sep='\n')