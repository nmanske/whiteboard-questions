from random import randint

class Node:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(n) for n in self]
        return ' -> '.join(values)

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        raise ValueError('Value not found in list')

    def delete(self, value):
        previous = None
        current = self.head
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        raise ValueError('Value not found in list')

    @classmethod
    def generate(cls, n, min, max):
        ll = cls()
        ll.head = None
        for i in range(n):
            ll.insert(randint(min, max))
        return ll
