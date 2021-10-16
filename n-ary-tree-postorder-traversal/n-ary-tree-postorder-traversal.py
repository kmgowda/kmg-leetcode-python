// https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        out = list()
        if root == None:
            return out
        st = list()
        st.append(root)
        vis = None
        while any(st):
            nd = st.pop()
            if not any(nd.children):
                out.append(nd.val)
                vis = nd
            else:
                if vis and vis == nd.children[-1]:
                    out.append(nd.val)
                    vis = nd
                else:
                    vis = None
                    st.append(nd)
                    for i in range(len(nd.children)-1, -1, -1):
                        st.append(nd.children[i])
        return out                
        