class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist():
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node = self.head

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete(self,data):
        if self.head is not None and self.head.data == data:
            self.head = self.head.next

        previous = None
        current = self.head
        while current is not None:
            if current.data == data:
                previous.next = current.next
            previous = current
            current = current.next

    def search(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

n1 = Linkedlist()
print(n1.add(10))
n1.add(20)
n1.add(30)

n1.print_list()



       
