// https://leetcode.com/problems/permutation-in-string

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        pCounter = Counter(s1)
        sCounter = Counter(s2[:len(s1)-1])
        for i in range(len(s1)-1,len(s2)):
            sCounter[s2[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
               return True  
            sCounter[s2[i-len(s1)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s2[i-len(s1)+1]] == 0:
                del sCounter[s2[i-len(s1)+1]]   # remove the count if it is 0
        return False        