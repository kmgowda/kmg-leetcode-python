// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        map1= {}        
        for key in hashmap:
            i =  hashmap[key]
            if i not in map1:
                map1[i]=list()
            map1[i].append(key)
            
        lt = list(map1.keys())
        lt.sort()
        ret = list()
        for i in range(len(lt)-1, -1, -1):
            for val in map1[lt[i]]:
                ret.append(val)
        return ret[0:k]        
                