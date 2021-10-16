// https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        H = len(nums)
        while i < H:
              print(nums)
              print("i= %d, H= %d" %(i, H))
              if nums[i] != val:
                    i+=1
              else:
                cur = i
                while i < H and nums[i]==val:
                    i+=1
                m = i
                n = cur
                while m < H :
                    nums[n] = nums[m]
                    n+=1
                    m+=1
                H-=(i-cur)
                i= cur
        return H       
                
                