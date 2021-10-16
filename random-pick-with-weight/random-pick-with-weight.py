// https://leetcode.com/problems/random-pick-with-weight

class Solution:

    def __init__(self, w: List[int]):
         self.sum = list(itertools.accumulate(w))
        

    def pickIndex(self) -> int:
        rand = random.randint(0, self.sum[-1] - 1)
        return bisect.bisect_right(self.sum, rand)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()