// https://leetcode.com/problems/n-ary-tree-level-order-traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        out = list()
        level = list()
        ret = list()
        
        if not root:
            return ret
        level.append(root)
        out.append(level)
        tmp = list()
        tmp.append(root.val)
        ret.append(tmp)
        i =0
        while i < len(out):
            level = out[i]
            tmp = list()
            tmp1 = list()
            for nd in level:
                for ch in nd.children:
                    tmp.append(ch)
                    tmp1.append(ch.val)
            if any(tmp):        
                out.append(tmp)
                ret.append(tmp1)
            i+=1
        return ret  
                
        
        