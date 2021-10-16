// https://leetcode.com/problems/rotate-array

class Solution(object):

    def reverse(self, a, l, h):
        while l < h:
              tmp = a[l]
              a[l] = a[h]
              a[h] = tmp
              l+=1
              h-=1
    
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    
        l = 0
        h = len(nums)
        
        if h == 0 or h == 1 or k == 0:
            return
        
        k = k%h
        
        self.reverse(nums, 0, h-k-1)
#        print(nums)
        self.reverse(nums, h-k, h-1)
#        print(nums)
        self.reverse(nums, 0, h-1)
#        print(nums)
            
            
                
            