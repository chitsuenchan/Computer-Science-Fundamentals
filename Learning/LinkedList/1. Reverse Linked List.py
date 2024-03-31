class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head_node):
        self.head = head_node

    def add_node_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_values(self):
        current = self.head
        string = ""

        while current:
            if current.value != None and current.next is not None:
                string += str(current.value) +" -> "
            elif current.value != None:
                string += str(current.value)
            current = current.next
        return string + "\n"

    def remove_value(self, value):
        current = self.head

        if current.value == value:
            self.head = current.next
            current.next = None
        else:
            while current:
                next_node = current.next

                if next_node is None:
                    break

                if next_node.value == value:
                    current.next = next_node.next
                    next_node.next = None
                    break
                else:
                    current = current.next

def reverse_linked_list(head):
    # Base case
    if head is None or head.next is None:
        return head

    # Recursive step
    p = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return p



print("LinkedList")
print("=====================================")
ll = LinkedList(Node(20))
ll.add_node_start(16)
ll.add_node_start(11)
ll.add_node_start(4)
print(ll.print_values())

""" 
Reverse Linked (in place) has time complexity of 0(n) 
    - printing the linked list is 0(n) where n is the number of nodes in the LinkedList
    - reversing the linked list is 0(n) where n is the number of nodes in the linked list (due to the recursive call stack)
    - Overall time complexity of 0(n)

Has a space compleixty of 0(n)
    - printing the values is 0(n) where the number of nodes in the linked list 
    - reversing is 0(n) where the number of nodes in the linked list
    - Overall space complexity of 0(n)
"""
print("Reversed LinkedList (in place)")
print("=====================================")
ll.head = reverse_linked_list(ll.head)
print(ll.print_values())


""" 
This method creates a new LinkedList object to store the reversed list
Space and time complexity are the same as previous method because we take the worst case which is 0(n) still for space and time.
"""
print("Reversed LinkedList (again)")
print("=====================================")
reverse_ll = LinkedList(reverse_linked_list(ll.head))
print(reverse_ll.print_values())



