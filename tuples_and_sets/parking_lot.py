number_of_cars = int(input())
parking = set()
for _ in range(number_of_cars):
    command, plate = input().split(', ')
    
    if command == 'IN':
        parking.add(plate)
    else:
        parking.discard(plate)

if parking:
    for car in parking:
        print(car)
else:
    print('Parking Lot is Empty')
