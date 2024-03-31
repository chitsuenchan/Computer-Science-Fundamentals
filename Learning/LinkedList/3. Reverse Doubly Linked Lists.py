from Classes.DoublyLinkedList import DoublyLinkedList
from Classes.Node import Node

"""
    Solution is done with recursion.
"""


# Helper function
def print_nodes(head):
    current_node = head
    string = ""
    while current_node:
        if current_node.next is None:
            string += "({0})".format(current_node.value)
        else:
            string += "({0}) <-> ".format(current_node.value)
        current_node = current_node.next
    print(string)

def reverse(head, prev=None):
    if head is None:
        return prev

    next_node = head.next
    head.next = prev
    if prev is not None:
        prev.prev = head  # Update the prev pointer of the previous node

    return reverse(next_node, head)


dll = DoublyLinkedList()
dll.add_node_to_beginning(4)
dll.add_node_to_beginning(3)
dll.add_node_to_beginning(2)
dll.add_node_to_beginning(1)

print("\nDoubly LinkedList BEFORE Reversal")
print("=============================")
dll.print_nodes()

print("\nDoubly LinkedList AFTER Reversal")
print("=============================")
reverse_head = reverse(dll.head)  # Returns the head node of the reversed LinkedList (i.e. NOT LinkedList object)
print_nodes(reverse_head)
print(reverse_head.next.next.prev.value)
