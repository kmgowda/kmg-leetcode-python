// https://leetcode.com/problems/inorder-successor-in-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorder_successor(self, root, p , found):
        node = None
        if root:
            found, node = self.inorder_successor(root.left, p, found)
            if node:
                return True, node
            if found:
                return True, root
            elif root == p:
                 found = True
            found, node = self.inorder_successor(root.right, p, found)
        return found, node    
                 
    
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        found, node = self.inorder_successor(root, p, False)
        return node
        