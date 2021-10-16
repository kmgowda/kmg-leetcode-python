// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def inorder(root, ret):
            if not root:
                return 
            inorder(root.left, ret)
            ret.append(root.val)
            inorder(root.right, ret)
            
        
        ret= list()
        inorder(root, ret)
        return ret[k-1] 