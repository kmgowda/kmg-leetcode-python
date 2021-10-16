// https://leetcode.com/problems/wiggle-sort-ii

import heapq

class Solution(object):
    def wiggleSort1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop() 
        for i in range(0, len(nums), 2): nums[i] = arr.pop()
            
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        def partition(a, l, h):
            i = l
            j = h
            while i < j:
                while i < h and a[l] >= a[i]:
                      i+=1
                while j > l and a[l] < a[j]:
                    j-=1
                if i < j:
                    a[i], a[j]=a[j], a[i]
            a[l], a[j] = a[j], a[l]
            return j
        
        def find_median(a, k):
            l = 0
            h = len(a)-1
            p = 0
            while p != k:
                 p = partition(a, l, h)
                 if p < k:
                    l = p+1
                 else:
                    h = p-1
            return a[k]        
                    
        half=(len(nums)+1)//2
        #find_median(nums, half)
        nums.sort()
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]               
                    