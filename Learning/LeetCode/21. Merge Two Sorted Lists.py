"""
    Attempting this again after seeing the solution
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeSortedLinkedList(l1, l2):

    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next


l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(4)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

printLinkedList(l1)
printLinkedList(l2)

printLinkedList(mergeSortedLinkedList(l1, l2))