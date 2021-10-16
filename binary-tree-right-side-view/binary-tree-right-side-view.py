// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def collect(node, depth):
            if node:
                if depth == len(lt):
                    lt.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        lt = []
        collect(root, 0)
        return lt