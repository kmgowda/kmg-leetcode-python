// https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        map={}
        for i, item in enumerate(list1):
            map[item] = i
        for i, item in enumerate(list2):
            if item in map:
                map[item]+=i
            else:
                map[item]=i
        cm=set(set(list1)&set(list2))
        min = -1
        minlt = list()
        for item in cm:
            if min == -1 or  map[item] < min:
                min = map[item]
                minlt.clear()
                minlt.append(item)
            elif min != -1 and map[item] == min:
                minlt.append(item)
        
        return minlt        