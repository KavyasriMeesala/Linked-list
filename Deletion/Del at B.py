'''Deletion at begin'''


class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
class LinkedList:
    def __init__(self):
        self.head= None
    def iab(self, data):
        newnode= Node(data)
        if not self.head:
            self.head= newnode
            return
        current= self.head
        while current.next:
            current=current.next
        current.next= newnode
    def deletebegin(self):
        if self.head is None:
            print("Empty=LL")
        else:
            print("Deleted node from beginning", self.head.data)
            self.head= self.head.next
    def display(self):
        current= self.head
        if not current :
            print("LL-Empty")
            return 
        while current:
            print(current.data, end='----')
            current = current.next
        print("None")
ll= LinkedList()
while True:
    print("\n LinkedList- Delete at beginning....")
    print(" 1. insert")
    print(" 2. display")
    print(" 3. delete at begin")
    print(" 4.Exit ")
    choice = input("Enter your choice : ")
    if choice =='1' :
        data = int(input("Enter a value to insert : "))
        ll.iab(data)
    elif choice == '2':
        ll.display()
    elif choice == '3':
        ll.deletebegin()
    elif choice == '4':
        print("Exit the operation....")
        break
    else:
        print("Enter only ....1/2/3/4")