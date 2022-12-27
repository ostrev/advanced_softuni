numbers = [float(x) for x in input().split()]
dict_numbers = {}
for num in numbers:
    if num not in dict_numbers:
        float_num = float(num)
        dict_numbers[num] = 0
    dict_numbers[num] += 1

for k, v in dict_numbers.items():
    print(f'{k:.1f} - {v} times')
