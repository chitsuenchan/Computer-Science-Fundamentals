from .Node import Node
class LinkedList:
    def __init__(self, head_value=None):
        self.head = Node(head_value)
        self.next = next

    def add_node_to_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def print_nodes(self):

        current_node = self.head
        string = ""

        while current_node:

            if current_node.next is None:
                string += "({0})".format(current_node.value)
            else:
                string += "({0}) ->".format(current_node.value)

            current_node = current_node.next
        print(string)
