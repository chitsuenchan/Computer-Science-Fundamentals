
"""
    Passes all tests
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):

        # Base Case
        if head is None or head.next is None:
            return head

        # Recursive Step
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_head