// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ma = None
        def maxpath(root):
            if not root:
                return 0
            
            left = maxpath(root.left)
            right= maxpath(root.right)
   
            if self.ma == None:
                self.ma = root.val+left+right
            else:    
                self.ma = max(self.ma, root.val+left+right, root.val+left, root.val+right)
            return max(root.val+left, root.val+right, root.val)
        if not root:
            return 0
        val = maxpath(root)
        
        return max(self.ma, val)