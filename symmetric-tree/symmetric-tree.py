// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque()
        if not root:
            return True
        if not root.right and not root.left:
            return True
        if not root.right or not root.left:
            return False
        q.append(root.left)
        q.append(root.right)
        while q:
            l = q.popleft()
            if not any(q):
                #print("KMG1")
                return False
            r = q.popleft()
            if l.val == r.val:
                if l.left and r.right:
                    q.append(l.left)
                    q.append(r.right)
                elif not (not l.left and not r.right):
                    #print("KMG2")
                    return False
                if l.right and r.left:
                    q.append(l.right)
                    q.append(r.left)
                elif not(not l.right and not r.left):
                    #print("KMG3")
                    return False
            else:
                #print("KMG4")
                return False
            
        return True    
                    