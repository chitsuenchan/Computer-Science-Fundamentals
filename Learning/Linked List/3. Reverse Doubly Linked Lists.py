from Classes.SinglyLinkedList import LinkedList
from Classes.Node import Node

def reverse(head, prev=None):
    if head is None:
        return prev

    next_node = head.next
    head.next = prev
    return reverse(next_node, head)

ll = LinkedList(5)

ll.add_node_to_beginning(4)
ll.add_node_to_beginning(3)
ll.add_node_to_beginning(2)
ll.add_node_to_beginning(1)

ll.print_nodes()

print(ll.head.value)
