number_of_commands = int(input())

parking = set()
for _ in range(number_of_commands):
    data = input().split(', ')
    if data[0] == 'IN':
        parking.add(data[1])
    elif data[0] == 'OUT':
        parking.remove(data[1])

if parking:
    print(*parking, sep='\n')
else:
    print("Parking Lot is Empty")