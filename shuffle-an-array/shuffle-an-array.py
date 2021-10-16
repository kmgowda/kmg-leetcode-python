// https://leetcode.com/problems/shuffle-an-array

class Solution:

    def __init__(self, a):
        self._orig = a[:]
        self._a = self._orig[:]

    def reset(self):
        self._a = self._orig[:]
        return self._a

    def shuffle(self):
        n, a = len(self._a), self._a
        for i in range(n):
            j = random.randint(i, n-1)
            a[i], a[j] = a[j], a[i]
        return a
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()