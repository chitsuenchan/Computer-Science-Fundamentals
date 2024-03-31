

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d


def printLinkedList(head):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next_node

printLinkedList(a)