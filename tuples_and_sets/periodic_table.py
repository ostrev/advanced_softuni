numbers = int(input())
elements = set()
for _ in range(numbers):
    data = input().split()
    elements.update(data)

print(*elements, sep='\n')