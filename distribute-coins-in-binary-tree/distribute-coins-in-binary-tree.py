// https://leetcode.com/problems/distribute-coins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs(root)
        return self.ans
        
    def dfs(self, node):
        if not node:
            return 0
        L = self.dfs(node.left)
        R = self.dfs(node.right)
        self.ans += abs(L) + abs(R)
        return node.val - 1 + L + R