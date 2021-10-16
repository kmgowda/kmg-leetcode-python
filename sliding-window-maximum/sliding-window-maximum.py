// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = list()
        if not len(nums):
            return ret
      
        m_pos = None
        e = k
        w = k
        while  e <= len(nums):
            b = e-w
            for j in range(b, e):
                if m_pos == None or nums[m_pos] < nums[j]:
                   m_pos = j
                
            if m_pos != None:
                ret.append(nums[m_pos])
            
            if m_pos <= b:
                m_pos = None
                w = k
            else:
                w = 1
            e+=1    
         

        return ret    