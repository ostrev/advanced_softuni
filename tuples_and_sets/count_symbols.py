text = input()
characters = {}

for char in text:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1

sorted_char = sorted(characters.items(), key=lambda x: x)
for char, times in sorted_char:
    print(f'{char}: {times} time/s')
