"""
    Purpose of this function is to print all the nodes from a Linked List
    when given the head
"""

def print_nodes_from_singly_linked_list(head):
    current_node = head
    string = ""
    while current_node:
        if current_node.next is None:
            string += "({0})".format(current_node.value)
        else:
            string += "({0}) -> ".format(current_node.value)
        current_node = current_node.next
    print(string)