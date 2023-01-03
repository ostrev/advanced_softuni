numbers = input().split()
n_num = int(numbers[0])
m_num = int(numbers[1])
first_set = set()
second_set = set()

for _ in range(n_num):
    line = int(input())
    first_set.add(line)
for _ in range(m_num):
    line_m = int(input())
    second_set.add(line_m)

new_set = first_set.intersection(second_set)

print(*new_set, sep='\n')
