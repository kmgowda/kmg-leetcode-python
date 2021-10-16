// https://leetcode.com/problems/maximum-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def get_tree(self, nums, f, l):
        if f > l:
            return None
        
        m = None
        for i in range(f, l+1):
            if m == None or nums[m] < nums[i]:
                m = i
     
        if m != None:
            root = TreeNode(nums[m])
            root.left = self.get_tree(nums, f, m-1)
            root.right = self.get_tree(nums, m+1, l)
        else:
            root = None
            
        return root    
            
    
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.get_tree(nums, 0, len(nums)-1)