// https://leetcode.com/problems/find-the-duplicate-number

class Solution(object):
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 1, len(nums)-1
        
        while l < h:
            m = (l+h)>>1
            
            c = 0
            for a in nums:
                if a <= m:
                   c+=1
            if c <= m:
                l = m+1
            else:
                h =m
        return l 
    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = fast = slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        while head != slow:
            head = nums[head]
            slow = nums[slow]

        return head