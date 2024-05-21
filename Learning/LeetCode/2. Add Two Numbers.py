"""
    Pass
    Beats 70%

    Difficulty 2/10 - Got relatively quickly for a medium
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):

    def findReversedSum(head):
        total = ""

        current = head
        while current:
            total += str(current.val)
            current = current.next
        return total[::-1]

    l1_sum = findReversedSum(l1)
    l2_sum = findReversedSum(l2)
    total_str = list(str(int(l1_sum) + int(l2_sum)))

    print(total_str)

    dummy = ListNode(0)
    current = dummy

    while total_str:
        last_element = total_str.pop()
        current.next = ListNode(int(last_element))
        current = current.next

    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
print_linked_list(result)