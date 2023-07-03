'''The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer,root , pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        #If no root return -1
        if not root:
            return -1
        
        #if we are on the edge of a tree on leaf node, there will be no left and no right and height here is 0
        if not root.left and not root.right:
            return 0
        #otherwise we will get the left height and right height of the nodes children by calling getheight recurrsively 
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        #Then we are gonna return 1+ max of left or right
        return max(left_height,right_height) + 1
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
