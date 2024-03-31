class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head_node):
        self.head = Node(head_node)

    def add_to_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print("Added new Node {0}".format(value))

    def print_all_nodes(self):

        current_node = self.head
        string = ""

        while current_node is not None:
            if current_node.next is None:
                string += " ({0})".format(current_node.value)
            else:
                string += " ({0}) -> ".format(current_node.value)
            current_node = current_node.next

        return string


def reverse_linked_list(head):

    if head is None or head.next is None:
        return head


    p = reverse_linked_list(head.next)

    print(head.value)
    return p

a = Node(10)

ll = LinkedList(5)
ll.add_to_start(4)
ll.add_to_start(3)
ll.add_to_start(2)
ll.add_to_start(1)

print(ll.print_all_nodes())
reverse_linked_list(ll.head)