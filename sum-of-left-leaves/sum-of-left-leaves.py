// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        
        def sumLeftleaf(root, isleft):
            if root:
                if not root.left and not root.right:
                    if isleft:
                        self.total+=root.val
                sumLeftleaf(root.left, True)
                sumLeftleaf(root.right, False)
                
        sumLeftleaf(root, False)
        return self.total