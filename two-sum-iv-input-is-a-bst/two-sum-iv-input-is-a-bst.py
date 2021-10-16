// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def binsearch(self, nums, f, l, target):
        if f > l:
            return False
      
        m = (f+l)>>1
        if nums[m] == target:
            return True
        elif nums[m] < target:
            return self.binsearch(nums, m+1, l, target)
        else:
            return self.binsearch(nums, f, m-1, target)
        
    def inorder(self, root, lt):
        if not root:
            return 
        self.inorder(root.left, lt)
        lt.append(root.val)
        self.inorder(root.right, lt)
        
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        lt = list()
        self.inorder(root,lt)
        for i, n in enumerate(lt):
            if self.binsearch(lt, i+1, len(lt)-1, k-n):
                return True
        return False    

                
        