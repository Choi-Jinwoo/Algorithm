class Node:
    def __init__(self, data):
        self.data = data
        self.marked = False
        self.adjacent = []

class Graph:
    def __init__(self, size):
        self.nodes = []
        for i in range(size):
            self.nodes.append(Node(i))

    def add_edge(self, i1, i2):
        n1 = Node(i1)
        n2 = Node(i2)

        if n1.adjacent

