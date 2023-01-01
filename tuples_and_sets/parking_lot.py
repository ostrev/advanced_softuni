number_of_commands = int(input())

parking = set()
<<<<<<< HEAD
for _ in range(number_of_commands):
    data = input().split(', ')
    if data[0] == 'IN':
        parking.add(data[1])
    elif data[0] == 'OUT':
        parking.remove(data[1])
=======
for _ in range(number_of_cars):
    command, plate = input().split(', ')
    
    if command == 'IN':
        parking.add(plate)
    else:
        parking.discard(plate)
>>>>>>> 64cb0a5479114a89dbe4edfbfa14c2345fc0f221

if parking:
    print(*parking, sep='\n')
else:
<<<<<<< HEAD
    print("Parking Lot is Empty")
=======
    print('Parking Lot is Empty')
>>>>>>> 64cb0a5479114a89dbe4edfbfa14c2345fc0f221
