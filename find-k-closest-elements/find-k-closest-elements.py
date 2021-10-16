// https://leetcode.com/problems/find-k-closest-elements

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = 0
        h = len(arr)-1
        
        while l <= h:
            m = (l+h)//2
            if arr[m] == x:
                break
            elif x > arr[m]:
                l = m+1
            else:
                h = m-1
        l = m-1
        r = m+1
        k-=1
#        print("m = %d" %m)
        while k > 0:
#            print("l = %d , r = %d" %(l, r))
            if l >= 0:
                ld = x-arr[l]
            else:
                ld = None
            if r < len(arr):
                rd = arr[r]-x
            else:
                rd = None
            if ld != None and rd != None:
                if ld <= rd:
                    l-=1
                else:
                    r+=1
            elif ld != None:
                 l-=1
            elif rd != None:
                 r+=1
            else:
                k=0
            k-=1
        ret = list()    
        for i in range(l+1,r):
            ret.append(arr[i])
        return ret
                
                
            
        