// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = -1
        self.first = root.val if root else -1
        
        def traverse(node):
            if node:
                if node.val > self.first and (self.ans == -1  or self.ans > node.val):
                    self.ans = node.val
                    return
                else:
                    traverse(node.left)
                    traverse(node.right)
        traverse(root)
        return self.ans