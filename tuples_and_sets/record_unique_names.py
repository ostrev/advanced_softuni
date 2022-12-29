number_of_names = int(input())
list_names = []
for _ in range(number_of_names):
    list_names.append(input())

set_names = set(list_names)

print(*set_names, sep='\n')