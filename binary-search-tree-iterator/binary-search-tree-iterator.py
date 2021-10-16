// https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def inorder(self, root, lt):
        if root:
            self.inorder(root.left, lt)
            lt.append(root.val)
            self.inorder(root.right, lt)
            
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.lt = list()
        self.inorder(root, self.lt)

    def hasNext(self):
        """
        :rtype: bool
        """
        return any(self.lt)
        

    def next(self):
        """
        :rtype: int
        """
        return self.lt.pop(0)
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())