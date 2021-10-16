// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st = list()
        if root == None:
            return st
        st.append(root)
        rt = list()
        while len(st):
            top = st.pop()
            if top.left:
                st.append(top)
                st.append(top.left)
            else:
                rt.append(top.val)
                while top.right == None and len(st):
                    top = st.pop()
                    rt.append(top.val)
                    
                if top.right:
                    st.append(top.right)
        return rt            