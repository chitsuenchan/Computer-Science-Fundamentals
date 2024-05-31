class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):

    def print_linked_list(head):
        s = ""
        current = head

        while current.next:
            s += str(current.val) + " -> "
            current = current.next
        s += str(current.val)

        print(s)

    def insert_copy_node(current):
        new_node = Node(current.val, current.next, current.random)

        new_node.next = current.next
        current.next = new_node

    print_linked_list(head)

    dummy = Node(0)
    current = head

    while current:
        print(current.val)
        insert_copy_node(current)

        if current.next is None:
            break
        current = current.next.next

    print_linked_list(head)

    return head

head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)

copyRandomList(head)