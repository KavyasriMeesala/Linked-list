'''Consider a single linked list with insert at end nodes after insertion reverse the node to print
input  -  11-22-33-44-55-null
output -  55-44-33-22-11-null
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='-')
            temp = temp.next
        print('null')
ll = SinglyLinkedList()
for value in [11, 22, 33, 44, 55]:
    ll.insert_at_end(value)

print("Original List:")
ll.print_list()

ll.reverse()

print("Reversed List:")
ll.print_list()


