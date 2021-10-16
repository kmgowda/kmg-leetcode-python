// https://leetcode.com/problems/count-of-smaller-numbers-after-self

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.count = 1
        self.val=val

class Solution(object):

    def InsertNode(self, root, val):
        if root is None:
            return 0
        rCount = 0
        while True:
            if val<=root.val:
                root.count+=1
                if root.left == None:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            else:
                rCount+=root.count
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return rCount
    
    
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if n==0:return []
        if n==1: return [0]
        
        ans = []
        root = TreeNode(nums[-1])
        ans.append(0)
        
        for i in range(n-2, -1, -1):
            count = self.InsertNode(root,nums[i])
            ans.append(count)
        return ans[::-1]           