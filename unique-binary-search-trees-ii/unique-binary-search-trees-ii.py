// https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        if n < 1: return []
        mem = {}
        
        def generate(start, end):
            if (start, end) in mem:
                return mem[(start, end)]
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            mem[(start, end)] = res
            return res
        
        return generate(1, n) 