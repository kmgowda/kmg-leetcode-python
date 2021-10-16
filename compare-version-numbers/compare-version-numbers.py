// https://leetcode.com/problems/compare-version-numbers

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        lt1 = version1.split('.')
        lt2 = version2.split('.')
        i =0
        j = 0
        while i < len(lt1) and j < len(lt2):
            if int(lt1[i]) > int(lt2[j]):
                return 1
            if int(lt1[i]) < int(lt2[j]):
                return -1
            i+=1
            j+=1
        while i < len(lt1):
            if int(lt1[i]) > 0:
                return 1
            i+=1
        while j < len(lt2):
            if int(lt2[j]) > 0:
                return -1
            j+=1  
        return 0