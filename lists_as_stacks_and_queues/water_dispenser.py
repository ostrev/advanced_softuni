from _collections import deque
quantity_of_water = int(input())
command = input()
people_drink_water = deque()

while command != 'Start':
    people_drink_water.append(command)
    command = input()

command = input()
while command != 'End':
    data = command.split()
    if data[0] == 'refill':
        liters = data[1]
        quantity_of_water += int(liters)
    else:
        liters = int(data[0])
        if quantity_of_water >= liters:
            print(f"{people_drink_water.popleft()} got water" )
            quantity_of_water -= liters
        else:
            print(f"{people_drink_water.popleft()} must wait")


    command = input()
print(f"{quantity_of_water} liters left")
