number_of_guests = int(input())

vip = set()

for _ in range(number_of_guests):
    code = input()
    vip.add(code)

command = input()
while command != 'END':
    vip.remove(command)
    command = input()


vip_sorted = sorted(vip)

print(len(vip))
print(*vip_sorted, sep='\n')
