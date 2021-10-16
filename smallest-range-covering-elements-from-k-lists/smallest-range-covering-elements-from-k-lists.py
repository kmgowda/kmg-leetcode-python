// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists

class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        
        ans = -float('inf'),float('inf')
        right = max(row[0] for row in nums)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
                
            if j+1 == len(nums[i]):
                break
            right = max(right, nums[i][j+1])
            heapq.heappush(pq, (nums[i][j+1], i, j+1))
 
        return ans     


    