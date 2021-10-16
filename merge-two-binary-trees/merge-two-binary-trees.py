// https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def merge(one, two):
            node = None
            if one or two:
                node = TreeNode(0)
                if one:
                    node.val+=one.val
                if two:
                    node.val+=two.val
                node.left = merge(one.left if one else None, two.left if two else None)
                node.right = merge(one.right if one else None, two.right if two else None)
            return node
        
        return merge(t1,t2)
            