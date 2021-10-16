// https://leetcode.com/problems/palindromic-substrings

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def count(st):
            cnt=0
            for i in range(0, len(st)):
                for j in range(1, len(st[i:])+1):
                    if st[i:i+j] and st[i:i+j] == ''.join(reversed(st[i:i+j])):
                        cnt+=1
            return cnt
        
        return count(s)
                