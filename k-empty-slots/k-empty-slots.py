// https://leetcode.com/problems/k-empty-slots

class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        garden = [[i - 1, i + 1] for i in range(len(bulbs))]
        garden[0][0], garden[-1][1] = None, None
        ans = -1
        for i in range(len(bulbs) - 1, -1, -1):
            cur = bulbs[i] - 1
            left, right = garden[cur]
            if right != None and right - cur == k + 1:
                ans = i + 1
            if left != None and cur - left == k + 1:
                ans = i + 1
            if right != None:
                garden[right][0] = left
            if left != None:
                garden[left][1] = right
        return ans       