from .Node import Node
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_to_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def add_node_to_beginning(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                return True
            current_node = current_node.next
        return False

    def print_nodes(self):

        current_node = self.head
        string = ""

        while current_node:

            if current_node.next is None:
                string += "({0})".format(current_node.value)
            else:
                string += "({0}) <-> ".format(current_node.value)

            current_node = current_node.next
        print(string)
