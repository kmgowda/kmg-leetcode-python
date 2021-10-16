// https://leetcode.com/problems/find-mode-in-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        lt=list()
        def inorder(root):
            if root:
                inorder(root.left)
                lt.append(root.val)
                inorder(root.right)
        
        inorder(root)
        d= collections.Counter(lt)
        ma = max([j for j in d.values()]+[0]) 
        out=list()
        for k in d:
            if d[k]==ma:
                out.append(k)
   
        return out
        