// https://leetcode.com/problems/binary-tree-vertical-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        d=collections.defaultdict(list)
        q=[(root,0)]
        for node,i in q:
            if node:
                d[i].append(node.val)
                q.append((node.left,i-1))
                q.append((node.right,i+1))
        ret=[0]*len(d) 
        diff=-min(d.keys())
       
        for k,v in d.items():
            ret[k+diff]=v
        return ret