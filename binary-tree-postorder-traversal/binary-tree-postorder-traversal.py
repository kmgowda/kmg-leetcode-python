// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st = list()
        if root == None:
            return st
        st.append(root)
        rt = list()
        visited = None
        while len(st):
            top = st.pop()
            if top.left == None and top.right == None:
                rt.append(top.val)
                visited = top
            else:
                if (top.left == visited or top.right == visited) and visited != None:
                    rt.append(top.val)
                    visited = top
                else:
                    st.append(top)
                    if top.right:
                        st.append(top.right)
                    if top.left:
                        st.append(top.left)
        return rt                