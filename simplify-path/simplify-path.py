// https://leetcode.com/problems/simplify-path

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        words = path.split('/')
        st = list()
        for word in words:
               if word =='..':
                    if st:
                        st.pop()
               elif word and word !='.':     
                    st.append('/'+word)
        if st:            
            return ''.join(st)
        else:
            return '/'