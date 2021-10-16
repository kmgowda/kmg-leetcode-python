// https://leetcode.com/problems/insert-into-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = TreeNode(val)
        if root == None:
            root = node
        else:
            cur = root
            while cur:
                if cur.val > val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = node
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = node
                        break
            return root            
                    
        