// https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.min = None
    
    def find_val(self, root, target, indiff):
     
        if root:
            if target > root.val:
                diff = target-root.val
            else:
                diff = root.val - target
            if indiff == None or diff < indiff:
                self.min = root.val
                indiff = diff
               
            if target <= root.val:
                self.find_val(root.left, target, indiff)
            else:    
                self.find_val(root.right, target, indiff)

    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.find_val(root, target,None)
        return self.min
        