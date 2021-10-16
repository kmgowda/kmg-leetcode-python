// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ma = 0
        lt = list()
        lt.append((root, 1))
        while lt:
            (node, cnt) = lt.pop()
            if node:
               left = node.left
               right = node.right
               if left:
                  if left.val == node.val+1:
                        lt.append((left, cnt+1))
                  else:
                        lt.append((left, 1))
               if right:
                  if right.val == node.val+1:
                        lt.append((right, cnt+1))
                  else:
                        lt.append((right, 1))
               ma = max(ma, cnt)
        return ma    