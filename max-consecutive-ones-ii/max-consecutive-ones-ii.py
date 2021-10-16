// https://leetcode.com/problems/max-consecutive-ones-ii

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = True
        ma = 0
        one = 0
        prv = 0
        for n in nums:
            if n == 1:
                one+=1
            elif flag:
                flag = False
                prv = one+1
                one = 0
            else:
                ma = max(ma,prv+one)
                prv = one+1
                one = 0
        return max(ma, one+prv)        