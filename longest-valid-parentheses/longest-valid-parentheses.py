// https://leetcode.com/problems/longest-valid-parentheses

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        st = list()
        st.append(-1)
        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans= max(ans, i-st[-1])
        return ans           
            