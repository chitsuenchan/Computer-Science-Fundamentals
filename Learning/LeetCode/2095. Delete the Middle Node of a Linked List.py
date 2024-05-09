
"""
    Passes all tests but it only beats like 20% of people
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node0 = ListNode(1)
node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(7)
node4 = ListNode(1)
node5 = ListNode(2)
node6 = ListNode(6)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

def deleteMiddle(head):
    current = head
    size = 0
    mid = 0

    if current.next == None:
        return None

    while current != None:
        current = current.next
        size += 1

    mid = size // 2

    def getNode(head, index):

        current = head
        current_idx = 0
        while current != None:
            if current_idx == index:
                return current
            current = current.next
            current_idx += 1

    node_before_mid = getNode(head, mid - 1)
    node_mid = node_before_mid.next

    node_before_mid.next = node_mid.next
    node_mid.next = None

    return head




ll = deleteMiddle(node0)

current = ll
while current != None:
    print(current.val)
    current = current.next