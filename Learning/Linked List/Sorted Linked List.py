class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head_node):
        self.head = head_node

    def add_node_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_values(self):
        current = self.head
        string = ""

        while current:
            if current.value != None and current.next is not None:
                string += str(current.value) +" -> "
            elif current.value != None:
                string += str(current.value)
            current = current.next
        return string + "\n"

    def remove_value(self, value):
        current = self.head

        if current.value == value:
            self.head = current.next
            current.next = None
        else:
            while current:
                next_node = current.next

                if next_node is None:
                    break

                if next_node.value == value:
                    current.next = next_node.next
                    next_node.next = None
                    break
                else:
                    current = current.next




## creating two linked lists
print("Linked List A")
print("=====================================")
lla = LinkedList(Node(40))
lla.add_node_start(22)
lla.add_node_start(8)
lla.add_node_start(1)
print(lla.print_values())

print("Linked List B")
print("=====================================")
llb = LinkedList(Node(20))
llb.add_node_start(16)
llb.add_node_start(11)
llb.add_node_start(4)
print(llb.print_values())


## Merge Sorted  Linked Lists

def sort_merge(node_a, node_b):
    if node_a is None:
        return node_b
    if node_b is None:
        return node_a

    if node_a.value < node_b.value:
        node_a.next = sort_merge(node_a.next, node_b)
        return node_a
    else:
        node_b.next = sort_merge(node_a, node_b.next)
        return node_b

ll_sort_merge = LinkedList(sort_merge(lla.head, llb.head))

print("Sorted Merged Linked List A and B")
print("=====================================")
print(ll_sort_merge.print_values())





