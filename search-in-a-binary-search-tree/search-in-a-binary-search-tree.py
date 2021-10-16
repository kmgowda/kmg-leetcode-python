// https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bst_serach(self, root, val):
        if root:
            if val == root.val:
                return root
            elif val < root.val:
                return self.bst_serach(root.left, val)
            else:
                return self.bst_serach(root.right, val)
        return root    
    
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.bst_serach(root,val)