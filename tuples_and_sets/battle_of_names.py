num = int(input())

odd_set = set()
even_set = set()
sum_of_name = 0
for i in range(1, num + 1):
    name = input()
    for ch in name:
        sum_of_name += ord(ch)
    sum_of_name = int(sum_of_name / i)
    if sum_of_name % 2 == 0:
        even_set.add(int(sum_of_name))
    else:
        odd_set.add(int(sum_of_name))
    sum_of_name = 0
if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
    print(*result, sep=", ")
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
    print(*result, sep=", ")
else:
    result = odd_set.symmetric_difference(even_set)
    print(*result, sep=", ")