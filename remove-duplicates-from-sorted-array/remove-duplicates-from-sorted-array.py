// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution(object):
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)
        while l < h:
#            print(nums)
            if l+1 >= h:
                break
            if nums[l] != nums[l+1]:
                l+=1
            else:
                l+=1
                i = l
                while i < h and nums[l] == nums[i]:
                      i+=1
                j = l        
                for k in range(i, h):
                    nums[j]=nums[k]
                    j+=1
 
                h -=(i-l)
        return h

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or not len(nums):
            return 0
        k = 0
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k]= nums[i]
                k+=1
        nums[k] = nums[-1]
        return  k+1       
    
    
    