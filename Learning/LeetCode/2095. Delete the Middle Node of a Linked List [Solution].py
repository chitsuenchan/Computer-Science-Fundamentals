class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle_node(head):
    if not head or not head.next:
        return None

    slow = fast = prev = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head


# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


# Example usage
if __name__ == "__main__":
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original linked list:")
    print_list(head)

    # Delete the middle node
    head = delete_middle_node(head)

    print("Linked list after deleting middle node:")
    print_list(head)
