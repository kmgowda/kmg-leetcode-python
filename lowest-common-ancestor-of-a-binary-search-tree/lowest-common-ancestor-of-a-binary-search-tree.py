// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor_rec(self, root, p, q):
        if root == None:
            return None, False
        left, lc = self.lowestCommonAncestor_rec(root.left, p, q)
        if lc:
            return left, lc
        right, rc =self.lowestCommonAncestor_rec(root.right, p, q)
        if rc:
            return right, rc
        
        if left and right:
            return root, True
        if root == p or root == q:
            if left or right:
                return root, True
            else:
                return root, False
        elif left:
            return left, False
        else:
            return right, False        
    
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node, flag = self.lowestCommonAncestor_rec(root, p, q)
        if flag:
            return node
        else:
            return None
 