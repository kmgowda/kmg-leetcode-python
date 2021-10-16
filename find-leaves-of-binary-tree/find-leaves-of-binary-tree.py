// https://leetcode.com/problems/find-leaves-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        
        def dfs(node):
            if not node:
                return 0
            depth = max(dfs(node.left),dfs(node.right))+1
            if len(ret)<depth:
                ret.append([])
            ret[depth-1].append(node.val)
            return depth
        
        dfs(root)
        return ret       