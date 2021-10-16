// https://leetcode.com/problems/find-median-from-data-stream

from heapq import heappush, heappop, heapreplace, heapify
class MedianFinder(object):

    def __init__(self):
        #keep smaller half (size >= 1)
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return ((-self.maxHeap[0] + self.minHeap[0])/2.0)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()