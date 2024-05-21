"""
    Needed solution
    Difficulty 8/10
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to hold the result
        dummy = ListNode(0)
        current = dummy

        # While both lists are not empty
        while l1 and l2:
            # Compare the values of the two lists
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # If one list is empty, append the rest of the other list
        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next
