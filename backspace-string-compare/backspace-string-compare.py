// https://leetcode.com/problems/backspace-string-compare

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def shrink(s):
            st, cnt = list(), 0
            for ch in s:
                if ch == '#':
                    if cnt > 0:
                        st.pop()
                        cnt-=1
                else:
                    st.append(ch)
                    cnt+=1
            return ''.join(st)
        
        return shrink(S) == shrink(T)
                    