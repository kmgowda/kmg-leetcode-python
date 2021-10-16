// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = None
        size = len(nums)
        if size:
            m = size//2
            root = TreeNode(nums[m])
            if size > 1:
                if m > 0:
                    root.left = self.sortedArrayToBST(nums[:m])
                if m+1 < size:    
                    root.right= self.sortedArrayToBST(nums[m+1:])
        return root
            
        
        