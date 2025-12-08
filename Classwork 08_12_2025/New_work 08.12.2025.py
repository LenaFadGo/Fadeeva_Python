stack_list = []

def push(val):
    stack_list.append(val)

def pop():
    val = stack_list[-1]
    stack_list.pop()
    return val

push(3)
push(5)
push(10)
print(stack_list)
