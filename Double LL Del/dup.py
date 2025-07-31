class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        """Display the list in 'DLL 10<-->20<-->...' format."""
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print("DLL ")
        print("<-->".join(elements))

    def print_duplicates(self):
        """Print duplicate elements with their frequencies."""
        freq = {}
        temp = self.head
        while temp:
            freq[temp.data] = freq.get(temp.data, 0) + 1
            temp = temp.next

        print("\nDuplicate Elements and Their Frequency:")
        has_duplicates = False
        for data, count in freq.items():
            if count > 1:
                print(f"{data} occurs {count} times")
                has_duplicates = True
        if not has_duplicates:
            print("No duplicates found.")

# Example usage
dll = DoublyLinkedList()
elements = [10,20,30,20,10,40]
for el in elements:
    dll.append(el)

dll.display()
dll.print_duplicates()
