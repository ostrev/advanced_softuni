line = input()
dic = {}
for char in line:
    if char not in dic:
        dic[char] = 1
    else:
        dic[char] += 1

for kvp in sorted(dic.items()):

    print(f'{kvp[0]}: {kvp[1]} time/s')
