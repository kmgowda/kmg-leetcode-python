// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rt = list()
        if root == None:
            return rt
        ret = list()
        tmp = list()
        tmp.append(root.val)
        ret.append(tmp)
        tmp= list()
        tmp.append(root)
        rt.append(tmp)
        index = 0
        while len(rt[index]):
            tmp = list()
            tmp1 = list()
            for i in range(len(rt[index])):
                node = rt[index][i]
                if node.left:
                    tmp.append(node.left)
                    tmp1.append(node.left.val)
                if node.right:
                    tmp.append(node.right)
                    tmp1.append(node.right.val)
            rt.append(tmp)
            ret.append(tmp1)
            index+=1
        ret.pop()   
        return ret    
            
            
        