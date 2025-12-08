class Stack:
    counter = 0


    def __init__(self):
        Stack.counter += 1
        self.__stack_list = []
        self.first = 1

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        print(self.__stack_list)
        val = self.__stack_list[-1]
        self.__stack_list.pop()
        return val

    def set_second(self):
        self.set_second = 2


stack_obj = Stack()
print(f"Экземпляр класса {stack_obj} имеет переиенные:", stack_obj.__dict__)
stack_obj.set_second()
print(f"Экземпляр класса {stack_obj} имеет переиенные:", stack_obj.__dict__)

print(stack_obj,__dict__)
# stack_obj_1 = Stack()
# print(f"Экземпляр класса {stack_obj_1} имеет переменные:", stack_obj_1.__dict__)





