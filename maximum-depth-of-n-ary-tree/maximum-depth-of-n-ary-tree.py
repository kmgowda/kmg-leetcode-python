// https://leetcode.com/problems/maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        max = 0
        if root:
            for ch in root.children:
                c_depth = self.maxDepth(ch)
                if c_depth > max:
                    max = c_depth
            max+=1
        return max    