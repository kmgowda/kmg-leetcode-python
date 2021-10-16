// https://leetcode.com/problems/construct-string-from-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        
        if t is None:
            return ''
        result = str(t.val)
        if t.left:
            result += '(' + self.tree2str(t.left) + ')'
            if t.right:
                result += '(' + self.tree2str(t.right) + ')'
        elif t.right:
            result += '()' + '(' + self.tree2str(t.right) + ')'
        return result
            