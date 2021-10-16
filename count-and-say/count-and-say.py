// https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        def count(st):
            ret=""
            c = 1
            for i in range(1, len(st)):
                if st[i] != st[i-1]:
                    ret+=str(c)+st[i-1]
                    c = 0
                c+=1
                
            return ret+str(c)+st[-1]
        
        ret="1"
        for i in range(1,n):
            ret=count(ret)
            #print(ret)
        return ret    
        
                