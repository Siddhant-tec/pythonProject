class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


ll = LinkedList()
ll.head = Node(3)
print(ll.head.data)
