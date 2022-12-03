string_parentheses = list(input())
stack_parentheses_index = []
for index in range(len(string_parentheses)):
    if string_parentheses[index] == '(':
        stack_parentheses_index.append(index)
    elif string_parentheses[index] == ')':
        start_index = int(stack_parentheses_index.pop())
        stop_index = int(index + 1)
        set_of_parentheses = string_parentheses[start_index:stop_index:]
        print(*set_of_parentheses, sep='')
