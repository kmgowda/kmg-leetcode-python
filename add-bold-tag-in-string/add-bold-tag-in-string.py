// https://leetcode.com/problems/add-bold-tag-in-string

class Solution(object):
    def addBoldTag(self, s, dic):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        lt = list()
        for k in dic:
            i=s.find(k)
            N = len(k)
            p=0
            while i != -1:
                lt.append((p+i, p+i+N-1))
                p += i+1
                i = s[p:].find(k)
            
        if not lt:
            return s
        lt.sort()
        out=list()
        e= -1
        p = -1
        for (x,y) in lt:
            if p == -1:
                p = x
            if e != -1 and x-1 > e:
                out.append((p,e))
                p = x
            e= max(e,y)
                    
        if not out or out[-1][1] != e:
            out.append((p,e))
        #print(lt)    
        #print(out)    
        st=''
        p = 0
        for (i,j) in out:
            st=st+s[p:i]+"<b>"+s[i:j+1]+"</b>"
            p = j+1
        st=st+s[p:]    
        return st            