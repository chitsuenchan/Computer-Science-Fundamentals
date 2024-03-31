from Learning.LinkedList.Classes.SinglyLinkedList import LinkedList
from Learning.LinkedList.Classes.Node import Node

def insertNodeAtPosition(head_node, data, position):

    current = head_node
    index = 0
    while current is not None:

        if index == position -1:

            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
        index += 1
        current = current.next
    return head_node


ll = LinkedList(3)
ll.add_node_to_beginning(2)
ll.add_node_to_beginning(1)
ll.print_nodes()

insertNodeAtPosition(ll.head, 4, 2)
ll.print_nodes()