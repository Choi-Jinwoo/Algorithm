class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None

    def enqueue(self, data):
        if self.__front is None:
            self.__front = Node(data)
            self.__rear = self.__front
        else:
            new_node = Node(data)
            self.__rear.next = new_node
            self.__rear = self.__rear.next

    def dequeue(self):
        data = self.__front.data
        self.__front = self.__front.next
        return data


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()

