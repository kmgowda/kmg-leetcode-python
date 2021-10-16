// https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def longpath(self, root):
        if not root:
            return 0, 0
        lc, lm = self.longpath(root.left)
        rc, rm = self.longpath(root.right)
        
        if root.left and root.right: 
            if root.left.val == root.val:
                lc+=1
            if root.right.val == root.val:
                rc+=1
            return (max(lc, rc), max(lc+rc, lm, rm))
        elif root.left and root.left.val == root.val:
             return (lc+1, max(lc+1, lm, rm))
        elif root.right and root.right.val == root.val:
            return (rc+1, max(rc+1, lm, rm))
        return (0, max(lm, rm))

    
    def longestUnivaluePath1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        c, m = self.longpath(root)
        return m

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursive(node):
            if node is None:
                return (0, 0)
            
            if node.left is None and node.right is None:
                return (0, 0)
            
            lres, ll = recursive(node.left)
            rres, rl = recursive(node.right)
            left = 0
            right = 0
            if node.left and node.right:
                
                if node.val == node.left.val:
                    left = 1 + ll
                if node.val == node.right.val:
                    right = 1 + rl
                
                return (max(lres, rres, left + right), max(left, right))
            
            if node.left:
                if node.val == node.left.val:
                    left = 1 + ll
                return max(lres, left), left
            if node.right:
                if node.val == node.right.val:
                    right = 1 + rl
                return max(rres, right), right
        return recursive(root)[0]   
    
    
    
            