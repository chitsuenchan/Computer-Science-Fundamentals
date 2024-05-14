"""
    Did not solve this one on my own

    Trick is
        - Use two pointers fast and slow
        - Eventually the fast pointer will catch up to the slow pointer if there is a cycle
        - If there isn't a cycle we check if the fast pointer is None or its next node is None then we know
            it's not a cycle and we return False
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
