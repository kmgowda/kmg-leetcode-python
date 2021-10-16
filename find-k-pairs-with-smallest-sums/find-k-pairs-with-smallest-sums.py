// https://leetcode.com/problems/find-k-pairs-with-smallest-sums

class Solution(object):
    
    # the below one works but memory limit exceeds
    def kSmallestPairs1(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        h={}
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 not in h:
                    h[n1+n2] =list()
                h[n1+n2].append((n1,n2))
        
        out=list()            
        for key in sorted(h.keys()):
            for pair in h[key]:
                out.append(pair)
                k-=1
                if not k :
                    return out
        return out 
    
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2: return []
        h = []
        
        # pair combination
        for i in range(len(nums1)):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))

        # return k smallest pairs
        res = []
        while h and k > 0:
            small, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        
        return res      
    