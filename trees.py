#a tree is different from the lined list it can have muktiple arro pointing towards many nodes this is bascially 
#called the tress it can branch to different nodes with info inside it.

# the most common is the binary tree each node has at most two children
class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

#the core rule of binary trees is that trees has a strict rule that the smaller data ex 30 should be at rhe left and the compartively larger one should be at the right so that is the basic rule.
class Tree():
    def __init__(self):
        self.root = None #exactly same as self.head which indicate the first node and in the tree the self.root does that.

    def insert(self,data):
        new_node = Node(data)
        current = self.root
        if self.root == None:
            self.root = new_node
            return
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if data > current.data:
                    if current.right is None:
                        current.right = new_node
                        return
                    else:
                        current = current.right

#transversal - inorder transversal - as we know in linked list there is a simple linear line to it so in this order tree as different paths so in the inorder traversal in order LEFT SUBTREE - CURRENT NODE - RIGHT SUBTREE
    def inorder(self,node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

#preorder traversal follows rule current , left , right
#it also suggest to print the current node immediately before even looking at its children


    def preorder(self,node):
        if node == None:
            return
        else:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node == None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def search(self,data):
        current = self.root
        while current is not None:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return (current.data)

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
           
t1 = Tree()
t1.insert(30)
t1.insert(20)
t1.insert(70)
t1.insert(40)
t1.insert(80)

t1.inorder(t1.root)
print(t1.search(40))
print(t1.find_min())
print(t1.find_max())

            
            
       
              


                
                

                   
                
            
       


       
        
          
            
            
        
   
