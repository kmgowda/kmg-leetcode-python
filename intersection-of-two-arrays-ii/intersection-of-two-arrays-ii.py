// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map={}
        for n in nums1:
             if n in map:
                 map[n]+=1
             else:
                 map[n]=1
        ret = list()
        for n in nums2:
            if n in map and map[n] > 0:
                map[n]-=1
                ret.append(n)
        return ret         
                