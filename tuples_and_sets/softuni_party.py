number_of_guests = int(input())
guest_list = set()
for _ in range(number_of_guests):
    line = input()
    guest_list.add(line)


command = input()
while command != 'END':
    guest_list.discard(command)
    command = input()


print(len(guest_list))
sorted_guest = sorted(guest_list)
for guest in sorted_guest:
    print(guest)