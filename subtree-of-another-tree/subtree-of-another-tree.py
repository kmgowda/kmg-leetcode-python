// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def compare(self, one, two):
        if not one and not two:
            return True
        if one and not two:
            return False
        if not one and two:
            return False
        if one.val != two.val:
            return False
        if self.compare(one.left, two.left):
            return self.compare(one.right, two.right)
        return False
        
    
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            if not t:
                return True
            else:
                return False
        if s.val == t.val:
            if self.compare(s, t):
                return True
        if self.isSubtree(s.left, t):
            return True
        return self.isSubtree(s.right, t)