// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left  and not root.right:
            return [str(root.val)]
        lt = self.binaryTreePaths(root.left)
        rt = self.binaryTreePaths(root.right)
        s = str(root.val)
        ret = []
        for word in lt+rt:
            if word:
                ret.append(s+"->"+word)
        return ret        
        
        
        