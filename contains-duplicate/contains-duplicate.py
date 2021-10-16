// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()
        for num in nums:
            if num in hash:
                return True
            hash.add(num)
        return False    