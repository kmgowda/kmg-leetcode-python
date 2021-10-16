// https://leetcode.com/problems/valid-parenthesis-string

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def isValid1(s, c):
            if not s:
                if not c:
                    return True
                else:
                    return False
            else:
                if s[0] == '(':
                    return isValid(s[1:], c+1)
                elif s[0] == ')' and c > 0:
                    return isValid(s[1:], c-1)
                elif s[0] == '*':
                    return isValid(s[1:], c+1) or isValid(s[1:], c-1) or isValid(s[1:], c)
                else:
                    return False

        if len(s) == 0:
            return True
        
        low = 0
        high = 0
        
        for c in s:
            
            if c == '(':
                low += 1
            else:
                low -= 1
            
            if c != ')':
                high += 1
            else:
                high -= 1
            
            if high < 0:
                break
            low = max(low, 0)
            
        return low == 0
                
 
            

                    
                
            