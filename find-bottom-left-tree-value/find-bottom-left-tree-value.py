// https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.left = None
        self.d = 0
           
        def leftmost(node, d):
            if node:
                if self.d < d: 
                    self.left = node.val
                    self.d = d
                leftmost(node.left,d+1)
                leftmost(node.right, d+1)
                
        leftmost(root,1)
        return self.left
                