// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dia = 0
        
        def maxDepth(root):
            if not root:
                return 0
            ld = maxDepth(root.left)
            rd = maxDepth(root.right)
            self.dia = max(self.dia, ld+rd)
            return max(ld,rd)+1
        maxDepth(root)
        return self.dia