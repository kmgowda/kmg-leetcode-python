// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = list()
        tmp = list()
        tmp.append(root)
        index = 0
        r = True
        while any(tmp):
            tmp1 = list()
            nxt = list()
            for node in tmp:
                tmp1.append(node.val)
            ret.append(tmp1)
            
            for i in range(len(tmp)-1, -1, -1):
                node = tmp[i]
                if r:
                    if node.right:
                       nxt.append(node.right)
                    if node.left :
                       nxt.append(node.left)
                else:
                    if node.left:
                       nxt.append(node.left)
                    if node.right:
                       nxt.append(node.right)                    
                         
           
            if r:
                r = False
            else:
                r = True
            tmp = nxt
        return ret    
            
            
                    
                  