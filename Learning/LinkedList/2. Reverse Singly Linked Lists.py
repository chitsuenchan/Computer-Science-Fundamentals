from Classes.SinglyLinkedList import LinkedList
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
            string += " ({0})".format(current_node.value)
        else:
            string += " ({0}) ->".format(current_node.value)
        current_node = current_node.next
    print(string)

def reverse(head):
    if head is None or head.next is None:
        return head

    reversed_list_head = reverse(head.next)
    head.next.next = head
    head.next = None

    return reversed_list_head

ll = LinkedList(5)
ll.add_node_to_beginning(4)
ll.add_node_to_beginning(3)
ll.add_node_to_beginning(2)
ll.add_node_to_beginning(1)

print("\nLinkedList Before Reversal")
print("=============================")
ll.print_nodes()

print("\nLinkedList After Reversal")
print("=============================")
reverse_head = reverse(ll.head)     # Returns the head node of the reversed LinkedList (i.e. NOT LinkedList object)


