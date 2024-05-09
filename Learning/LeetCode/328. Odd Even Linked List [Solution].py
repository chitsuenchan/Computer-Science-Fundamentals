class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = head
    even_head = head.next
    odd = odd_head
    even = even_head

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return odd_head


# Example usage
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("NULL")


# Example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
print_linked_list(head)

head = oddEvenList(head)

print("Linked list after rearranging odd and even nodes:")
print_linked_list(head)
