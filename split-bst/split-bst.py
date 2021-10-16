// https://leetcode.com/problems/split-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
             
        if not root:
            return [None,None]
        if root.val==V:
            a=root.right
            root.right=None
            return [root,a]
        elif root.val<V:
            small,large=self.splitBST(root.right,V)
            root.right=small
            return [root,large]
        else:
            small,large=self.splitBST(root.left,V)
            root.left=large
            return [small,root]
        
    
        
                
                   