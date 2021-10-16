// https://leetcode.com/problems/closest-binary-search-tree-value-ii

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = []
        self.index = 0
    
        self.traverse(root, target, k, res)

        return res
    
    def traverse(self, root, target, k, res):
        if not root:
            return res

        self.traverse(root.left, target, k, res)
    
        if len(res) < k:
            res.append(root.val)
        else: 
            if abs(target - res[self.index]) > abs(target - root.val): 
                res[self.index] = root.val
                self.index += 1
                if self.index == k:
                    self.index = 0
            else:
                return 
    
        self.traverse(root.right, target, k, res)
    
