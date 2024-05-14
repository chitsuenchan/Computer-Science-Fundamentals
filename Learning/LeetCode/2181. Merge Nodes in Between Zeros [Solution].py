"""
    Passes
    Beats 91%
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def merge_nodes(head):
    slow = head
    fast = head.next
    total = 0

    while fast and fast:
        print("Current fast node:", fast.val)
        total += fast.val
        print(" total:", total)

        if fast.val == 0:
            slow.val = total
            total = 0
            if fast.next:
                slow = slow.next
            else:
                slow.next = None

        fast = fast.next

    slow.next = None

    return head


head = ListNode(0)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(0)

print_linked_list(head)
merge_nodes(head)
print_linked_list(head)
