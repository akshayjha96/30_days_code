'''Today, we’re going to work with Binary Search Trees in more depth. We’re going to write an algorithm to do a level-order traversal of a binary tree. This is the underlying method of the famous breadth-first search algorithm.
A level-order traversal of a tree involves traversing or visiting each of the nodes on a tree in order by level. So the nodes will be visited in order of depth, the root node will be visited first, then its children will be visited, then its grand children will be visited, then its great-grandchildren and so on and so forth.
In our example tree below, that would mean visiting 3 first. Then visiting its children 2 and 5. And finally visiting its grand children 1, 4, and 7
What is important in breadth first search or a level order traversal is that we do not go from one level to another level without first exhausting all the nodes on the previous level. For instance we we should never visit 1, 4, or 7 before we we have visited all the nodes on the previous level.
Breadth First Search is useful when we are doing a nearest neighbor search. Imagine instead of numbers on our tree, we were searching city blocks. If we wanted to find the nearest gas station in a city on a grid pattern, we would want to use breadth first search to ensure that the first city block we get to with a gas station is also the closest gas station to us. So we start the search at our current block or the root of our tree. Then we search all our neighboring blocks, then their neighboring blocks, then their neighboring blocks and so on. If we find a gas station 4 blocks away, we will be able to say with confidence there is no closer gas station since by using Breadth-First Search we know we searched all the blocks 1, 2, and 3 away for gas stations and found none before searching blocks 4 away.
So how do we implement a level order traversal? HackerRank tells us a queue might be helpful. Why is that? If you need a refresher on queues vs stacks, you should rewatch my video on Day 18 of this series.
A queue is first in first out. We will leverage this to ensure the order in which we traverse nodes as we discover adjacencies. When we start at the root, we will look at its children and add them to the queue. We will traverse each node by popping it from the front of the queue and visiting it – so we pop 3 from the queue to look at it. We check to see if 3 has children and find 2 and 5. Our queue is now 2 and 5. Since 2 was added first, we will then pop it from the front of the queue to visit it and discover if it has children. It has a child “1” so we add it to the queue. Now our queue has 5 followed by 1. We will pop 5 from the queue and visit it to discover that it has 2 children “4”, and “7”. We will add those to the queue and now our queue has “1, 4, 7” which is the next level to traverse.
If we used a stack instead, we would have started the with just 3 in the stack. Then we would have popped it and found 2 and 5. We would have popped 5 from the top of the stack since it was added after 2, then added 4 and 7. So our stack would have 7 on top, then 4, then 2. We would have visited 7 then 4, then 2, then 1. That is the equivalent of a Depth First traversal or Depth First Search.
Let’s implement the levelOrder method. We’re continuing to use the node and tree code from yesterday so HackerRank will help us to initialize a tree and it will call levelOrder with the root of the tree.
We need to first initialize our queue. We will use a list in python as our working queue since we can append to the end of the list and pop from the beginning of the list to use it like a queue.
We will also make a string to keep track of which nodes we have traversed.
We will start off our queue with the root node we will traverse. In a disconnected graph or if you are searching multiple trees, you will seed your queue with all the roots at this point.
Then while, we the queue is not empty, or while we still have nodes to search, we will pop off the front node and traverse it. If it has children, we will add it to the queue. Then we will add it to the string of nodes we have searched that we will output in the end.
This loop will run while we continue to discover new nodes to visit until we have visited all connected nodes in the tree. Then we will exit and print the nodes we have visited.
'''

import sys

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

    def levelOrder(self,root):
        #Write your code here
        nodes_to_search = list()
        nodes_traversed = ''
        nodes_to_search.append(root)
        
        while len(nodes_to_search) >0:
            node = nodes_to_search.pop(0)
            if node.left:
                nodes_to_search.append(node.left)
            if node.right:
                nodes_to_search.append(node.right)
            nodes_traversed += str(node.data) + " "
        print(nodes_traversed)
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
