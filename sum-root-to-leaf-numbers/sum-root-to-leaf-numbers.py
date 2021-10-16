// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def get_sums(self, root, val):
        if not root:
            return 0
        
        val+=root.val
        if not root.left and not root.right:
            return val
          
        return self.get_sums(root.left, val*10)+self.get_sums(root.right, val*10)
        


    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_sums(root, 0)
        