// https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kmg_count(self, root):
        if root == None:
            return 0, True
        if root.left == None and root.right == None:
            return 1, True
        
        left , lc = self.kmg_count(root.left)
        right, rc = self.kmg_count(root.right)
        
        if lc == False or rc == False:
            return left+right, False
        
        if root.left:
            if root.val == root.left.val:
                flag = True
            else:
                flag = False
        else:
            flag = True
        if flag and root.right:
            if root.val == root.right.val:
                flag = True
            else:
                flag = False
        if flag:
            return left+right+1, True
        else:
            return left+right, False        
    
    
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret, flag = self.kmg_count(root)
        return ret