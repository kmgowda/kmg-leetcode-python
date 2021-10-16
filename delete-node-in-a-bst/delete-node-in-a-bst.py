// https://leetcode.com/problems/delete-node-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        prev = root
        next = None
        cur = root
        
        while cur:
            if cur.val == key:
                if cur.left != None and cur.right != None:
                   prev = cur
                   next = cur.right
                   while next.left:
                         prev = next
                         next = next.left
                   cur.val = next.val
                   cur = next

                if cur.left:
                    next = cur.left
                elif cur.right:
                    next = cur.right
                else:
                    next = None
                
                if cur == root:
                    root = next
                elif prev.left == cur:
                    prev.left = next
                elif prev.right == cur:
                    prev.right = next
                del cur
                cur = None
            elif cur.val > key:
                 prev = cur
                 cur = cur.left
            else:
                 prev = cur
                 cur = cur.right
                
        return root                