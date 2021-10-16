// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
       
    def preorderTraversal(self, root):
        st = list()
        lt = list()
        if root == None:
            return lt 
        st.append(root)
        while len(st):
            node = st.pop()
            lt.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return lt         
                
        