// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countNodes(root.left)+self.countNodes(root.right)+1 if root else 0