from _collections import deque
kids_names = deque(input().split())
toss = int(input())

count = 1
while len(kids_names) > 1:
    kid = kids_names.popleft()

    if count == toss:
        print(f"Removed {kid}")
        count = 0
    else:
        kids_names.append(kid)
    count += 1

print(f"Last is {''.join(kids_names)}")
