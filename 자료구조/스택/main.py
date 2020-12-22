
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.__top = None

    def push(self, data):
        if self.__top is None:
            self.__top = Node(data)
        else:
            new_node = Node(data)

            p = self.__top
            while p.next is not None:
                p = p.next

            p.next = new_node

    def pop(self):
        p = self.__top
        while p.next.next is not None:
            p = p.next

        data = p.next.data
        p.next = None

        return data

    def peek(self):
        p = self.__top
        while p.next is not None:
            p = p.next

        return p.data


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.peek())
