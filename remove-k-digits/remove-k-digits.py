// https://leetcode.com/problems/remove-k-digits

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        def shrink(num):
            for i in range(len(num) - 1):
                if num[i] > num[i + 1]:
                    return num[:i] + num[i+1:]
            return num[:-1]
        
        for i in range(k):
            num = shrink(num)
        
        return str(int(num)) if num else "0"