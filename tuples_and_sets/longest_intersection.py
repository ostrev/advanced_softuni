num = int(input())

first_set = set()
second_set = set()
longest_set = set()
for _ in range(num):
    line = input().split('-')
    range_set_first = [int(s) for s in line[0].split(',')]
    range_set_second = [int(s) for s in line[1].split(',')]
    for i in range(range_set_first[0], range_set_first[1] + 1):
        first_set.add(i)
    for n in range(range_set_second[0], range_set_second[1] + 1):
        second_set.add(n)

    inter_set = first_set.intersection(second_set)
    if len(inter_set) > len(longest_set):
        longest_set = inter_set

    first_set.clear()
    second_set.clear()

print(f'Longest intersection is {list(longest_set)} with length {len(longest_set)}')