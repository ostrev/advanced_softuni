from _collections import deque
line = input()
queue = deque()
while line != 'End':
    if line != 'Paid':
        queue.append(line)
    else:
      while queue:
          print(queue.popleft())

    line = input()
print(f"{len(queue)} people remaining.")
