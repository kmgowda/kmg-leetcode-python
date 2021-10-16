// https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = list()
        for ch in s:
            if ch == ']':
                tmp=""
                ch=""
                while st and ch != '[':
                    tmp=ch+tmp
                    ch = st.pop()
               
                tmp1=""
                while any(st):
                    c = st.pop()
                    if c.isdigit():
                        tmp1=c+tmp1
                    else:
                        st.append(c)
                        break
                if len(tmp1):        
                   n = int(tmp1)
                else:
                   n = 1
                tmp1=""
                for i in range(n):
                    tmp1+=tmp
                #print(tmp1)    
                for c in tmp1:
                    st.append(c)
            else:
                st.append(ch)
        #print(st)
        out=""        
        while st:
            out+=st.pop(0)
        
        
        return out        
                
                    