from Learning.LinkedList.Classes.SinglyLinkedList import LinkedList
from Learning.LinkedList.Classes.Node import Node
from Learning.LinkedList.HelperFunctions.printNodesFromLinkedListHead import print_nodes_from_singly_linked_list

"""
    Solution differs slightly from Hackerrank
        - We use our own Node and LinkedList classes here for testing purposes
        - In the Hackerrank version we get passed in a Node which had the property .data instead of .value
    
    Approach
        - Create pointers for both linked lists current nodes
        - Create a dummy node for the start of the merged linked list
        - Check the values if lla and llb nodes to compare which is smaller
            - add the smaller one to the merged current node next node
            - Increase pointers nodes by going to the next nodes
"""

def mergeLists(head_a, head_b):

    current_a = head_a
    current_b = head_b

    dummy_node = Node(None)
    current = dummy_node

    while current_a and current_b:

        if current_a.value < current_b.value:
            current.next = current_a
            current_a = current_a.next
        elif current_a.value > current_b.value or current_a.value == current_b.value:
            current.next = current_b
            current_b = current_b.next

        current = current.next

    if current_a:
        current.next = current_a
    elif current_b:
        current.next = current_b

    return dummy_node.next


lla = LinkedList(7)
lla.add_node_to_beginning(3)
lla.add_node_to_beginning(1)
lla.print_nodes()

llb = LinkedList(2)
llb.add_node_to_beginning(1)
llb.print_nodes()

mll = mergeLists(lla.head, llb.head)

print_nodes_from_singly_linked_list(mll)