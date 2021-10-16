// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        self.root = None       
        def insert(node):
            if not self.root:
                self.root = node
            else:
                cur = self.root
                while cur:
                    if node.val < cur.val:
                        if not cur.left:
                            cur.left = node
                            cur = None
                        else:
                            cur = cur.left
                    elif not cur.right:
                        cur.right = node
                        cur = None
                    else:
                        cur = cur.right
                        
        for n in preorder:
            insert(TreeNode(n))
        return self.root    
            