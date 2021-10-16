// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
           return "null" 
        q = list()
        q.append(root)
        i = 0
        while i < len(q):
            node = q[i]
            if node:
                q.append(node.left)
                q.append(node.right)
            i+=1

        while not q[-1]:
            q.pop()
        node = q.pop(0)    
        s = "["+str(node.val)
        while any(q):
            node = q.pop(0)
            s+=","
            if node:
                s+=str(node.val)
            else:
                s+="null"
        s+="]"
        return s
            
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 1:
            return None
        s = data[1:-1]
        lt = s.split(',')
        if lt[0] == "null" or lt[0] == "ul":
            return None
        root =  TreeNode(int(lt[0]))
        q = list()
        q.append(root) 
        i = 1
        while i < len(lt):
            par = q.pop(0)
            word = lt[i]
            if word != "null" and word !="ul":
                node = TreeNode(int(word))
                par.left = node
                q.append(node)
            i+=1
            if i >= len(lt):
                 break
            word = lt[i]
            if word != "null" and word !="ul":
                node = TreeNode(int(word))
                par.right = node
                q.append(node)
            i+=1
            
        return  root       
                    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))