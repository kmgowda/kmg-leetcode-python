// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = list()
        for ch in s:
            if ch in ('(', '{', '['):
                st.append(ch)
            else:
                if not any(st):
                    return False
                top = st.pop()
                if ch == ')' and top == '(':
                    continue
                if ch == ']' and top  == '[':
                    continue
                if ch == '}' and top == '{':
                    continue
                return False 
        if any(st):
            return False
        return True    
                
                
                
                
                
                    
        
        