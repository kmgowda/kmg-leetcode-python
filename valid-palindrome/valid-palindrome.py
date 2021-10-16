// https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = len(s)-1
        l = 0
        while l < h:
              if not s[l].isalnum():
                    l+=1
                    continue
              if not s[h].isalnum():
                    h-=1
                    continue
              if s[l].upper() != s[h].upper():
                  return False
              l+=1
              h-=1
        return True        
                    
                    
                
        
        