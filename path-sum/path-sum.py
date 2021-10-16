// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
           return False
        else:
            if root.val == sum and (root.left == None and root.right == None):
                return True
            elif root.left:
                ret = self.hasPathSum(root.left, sum-root.val)
            else:
                ret = False
            if ret == False and root.right:
                return self.hasPathSum(root.right, sum-root.val)
            else:
                return ret