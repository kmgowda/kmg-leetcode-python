// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        qu = list()
        tmp = list()
        tmp.append(root)
        qu.append(tmp)
        i = 0
        while i < len(qu):
            lt = qu[i]
            if lt != None:
               prev= None
               tmp = list()
               for node in lt:
                   if prev:
                      prev.next =node
                   prev = node  
                   if node.left:
                      tmp.append(node.left)
                   if node.right:
                      tmp.append(node.right) 
               if any(tmp):         
                  qu.append(tmp) 
            i+=1
        