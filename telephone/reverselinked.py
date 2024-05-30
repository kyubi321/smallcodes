class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Driver code
head = Node(85)
head.next = Node(15)
head.next.next = Node(4)
head.next.next.next = Node(20)

print("Given linked list:")
print_linked_list(head)

head = reverse_linked_list(head)

print("\nReversed linked list:")
print_linked_list(head)