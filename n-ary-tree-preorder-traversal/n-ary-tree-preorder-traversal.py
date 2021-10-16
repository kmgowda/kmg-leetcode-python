// https://leetcode.com/problems/n-ary-tree-preorder-traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
       
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        st = list()
        out = list()
        if root == None:
            return out
        st.append(root)
        while any(st):
            node = st.pop()
            out.append(node.val)
            for i in range(len(node.children)-1, -1, -1):
                st.append(node.children[i])
        return out        
                
            