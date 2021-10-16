// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    def rec_serialize(self, root):
        st=""
        if root:
            if not any(root.children):
                 return str(root.val)
            st +=str(root.val)+" ["
            flag = True
            for ch in root.children:
                if flag:
                    flag = False
                    st += self.rec_serialize(ch)
                else:    
                    st += " "+self.rec_serialize(ch)
            st +="]"
        return st    
                
                
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        ret = "["+self.rec_serialize(root)+"]"
#        print("KK  "+ret)
        return ret
        
    def rec_deserialize(self, data, index, N):
        root = None
        if index < N:
            while index < N and (data[index] == ' ' or data[index] =='['):
                index +=1
            st=''
            while index < N and data[index] !=' ' and data[index] !='[' and data[index] !=']':
                   st += data[index]
                   index += 1
            if st !='':
                val = int(st)
                root = Node(val, list()) 
                while index < N and data[index] == ' ':
                       index +=1
                if index < N and data[index] == '[':        
                    while True:
                          tmp, index = self.rec_deserialize(data, index, N)
                          if not tmp:
                                break
#                          print("root : %d  , child : %d" %(root.val, tmp.val))      
                          root.children.append(tmp)
            else:
                if index < N and data[index] ==']':
                    index+=1
                    
        return root, index        


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
#        print("In " + data)
        root, index = self.rec_deserialize(data,0,len(data))
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))