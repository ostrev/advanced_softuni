string_as_stack= list(input())

while string_as_stack:
    print(''.join(string_as_stack.pop()), end='')
