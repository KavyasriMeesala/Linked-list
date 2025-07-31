class Node:
    def __init__(self,data):
        self.data= data
        self.prev= None
        self.next= None
class DoublyLinkedList:
    def __init__(self):
        self.head= None
    def iae(self,data):
        newnode= Node(data)
        if not self.head:
            self.head=newnode
            return
        temp= self.head
        while temp.next:
            temp= temp.next
        temp.next= newnode
        newnode.prev= temp
    def dbv(self, value):
        temp= self.head
        while temp:
            if temp.data== value:
                print(f"Deleted:{temp.data}")
                if temp.prev:
                    temp.prev.next= temp.next
                else:
                    self.head= temp.next
                if temp.next:
                    temp.next.prev= temp.prev
                return
            temp= temp.next
        print(f"{value} not found in the list")
    def display(self):
        temp= self.head
        print("Doubly Linked List")
        while temp:
            print(temp.data, end="<-->")
            temp= temp.next
        print("None")
dll= DoublyLinkedList()
n= int(input("Enter the number of elements to insert at end: "))
for i in range(n):
    val=int(input(f"Enter element {i+1}: "))
    dll.iae(val)
dll.display()
d= int(input("\nHow many times you want to perform delete op: "))
for _ in range(d):
    val=int(input("Enter value to delete: "))
    dll.dbv(val)
    dll.dispaly()