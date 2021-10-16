// https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(root):
            if not root:
                return root
            l = invert(root.left)
            r = invert(root.right)
            root.left, root.right=r,l
            return root
        return invert(root)
            
            
        
      
            
            