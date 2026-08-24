#stcak is a bascially a data type take it as a stack of plate that the plate can be added at the top and only the plate is removed from the top also 
#the LIFO - last in first out 
#stack is done in two operations stack uses push - add , pop - remove the data type.

"""stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

top = stack.pop() #pop - remove and returns the last time
print(top)
print(stack)"""

"""ex = stack = []
stack.append(7)
stack.append(8)
stack.append(9)
stack.append(10)
print(stack)

index = 0
while stack:
    top = stack.pop()
    print(top)
    index +=1"""

#queue bascially by the name it is bascially a real queue/line type at a shop whoever joins first gets served first. new people joins at back and people leave from the front.
# it is like the first in the first out - FIFO

"""from collections import deque

queue = deque()
queue.append(10) #add to back
queue.append(20)
queue.append(30)
print(queue)

front = queue.popleft() #remove from the Front
print(front) # 10 the first one in the first one out
print(queue)

#note - .append() still ends to the back but .popleft() removes from the front instead of the end 
# deque is a function that is capable from removinf g=from both end and start.
# collection is a module that has different tools that are built in feature in python.
#queue = deque() means that make a new fresh object and name that deque as queue which is a variable

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

while queue:
    front = queue.popleft()
    print(front)

print(queue)"""

#The core idea: instead of storing a bunch of items together in one container (like a list does), a linked list is a chain of individual nodes, where each node holds: 1. some data , 2. a pinter(refernce) to the next node in the chain
# take it as a treasure hunt - when one clue leads u to the another clue then to the treasure. the treasure means null when the last pinter will point towards the null that means it is the end of linked notes.
# every new node starts with self.next = none - meaning "i dont know what comes after me"
#they will link manually

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3



"""class LinkedList:
    def __init__(self):
        self.head = None  #query

    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node"""

#self.head is the indicator which only indicate the starting node of the list 
#the current is equal to self.head because self.head if we do .next it will lost the starting pooint of the list
#so we use current .next for the same puropose so self.head is only a indicator that indicate the stating point of the list.



class LinkedList():
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete(self,data):
        if self.head is not None and self.head.data == data:
            self.head = self.head.next
            return

        previous = None
        current = self.head
        while  current is not None:
            if current.data == data:
                previous.next = current.next
                return 
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
            
                
           
n2 = LinkedList()
n2.add(10)
n2.add(20)
n2.add(30)

n2.print_list()
print(n2.search(20))


    





           
     
            


    


    





        







        



            
                
           
    

