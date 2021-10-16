// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorder_list(self, root, lt):
        if root:
            self.inorder_list(root.left, lt)
            lt.append(root.val)
            self.inorder_list(root.right, lt)
            
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lt = list()
        self.inorder_list(root, lt)
        for i in range(1, len(lt)):
            if lt[i-1] >= lt[i]:
                return False
        return True    
            
              