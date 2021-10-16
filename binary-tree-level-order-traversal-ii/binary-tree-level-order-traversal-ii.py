// https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d= collections.defaultdict(list)
        
        def preorder(root, l):
            if root:
                d[l]+=[root.val]
                preorder(root.left, l+1)
                preorder(root.right, l+1)
        preorder(root, 0)
        ret=list()
        for i in range(len(d)-1, -1, -1):
            ret.append(d[i])
        return ret    
        