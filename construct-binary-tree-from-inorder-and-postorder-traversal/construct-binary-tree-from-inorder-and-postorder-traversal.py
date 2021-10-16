// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
#class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def in_post_buildTree(self, inorder, ins, ine, postorder, ps, pe):
        if ine <= ins or pe <= ps:
            return None
        root = TreeNode(postorder[pe-1])
        pos = 0 
        for i in range(ins, ine, 1):
            if inorder[i] == root.val:
                pos = i
                break
        ll = pos-ins
        root.left = self.in_post_buildTree(inorder, ins, pos, postorder, ps, ps+ll)
        root.right = self.in_post_buildTree(inorder, pos+1, ine, postorder, ps+ll, pe-1)
        return root    
            
    
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.in_post_buildTree(inorder, 0, len(inorder), postorder, 0, len(postorder))
                
                