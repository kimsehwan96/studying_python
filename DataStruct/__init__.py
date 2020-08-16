class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item
    
    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size