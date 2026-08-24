#trees 
"""class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree():
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        current = self.root
        if self.root is None:
            self.root = new_node
            return
        while True:
            if current is  None:
                if data>current.data:
                    current.left = new_node
                else:
                    current = current.left
            else:
                if data<current.data:
                    if current.right is None:
                        current.right = new_node
                else:
                    current = current.right

    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.left)
        print(node)
        self.inorder(node.right)

    def preorder(self,node):
        if node == None:
            return
        print(node)
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self,node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node)

    def search(self,data):
        current = self.root
        while current is not None:
            if current.data == data:
                return True
            elif data>current.left:
                current = current.left
                return True
            else:
                current = current.right
                return True
        return False

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data"""

#hash value
"""class HashValue():
    def __init__(self):
        self.size = 10
        self.slots = [[] for _ in range(self.size)]

    def put(self,key,value):
        index = hash(key)%self.size
        value = self.slots[index]
        value.append((key,value))

    def get(self,key):
        index = hash(key)%self.size
        value = self.slots[index]
        for info in value:
            if info[0] == key:
                return info[1]
        return ("python can't find your value")

    def delete(self,key):
        index = hash(key)%self.size
        value = self.slots[index]
        for info in value:
            if info[0] == key:
                value.remove(info)
                return
            return "the value don't exists"""

#merge and merge_sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)


def merge(left,right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    result = result+left[i:]
    result = result+right[j:]
    return result

#loda ka suwar
list = [5,3,4,2]
print(merge_sort(list))

print("hello")


    










           

        
                

           

