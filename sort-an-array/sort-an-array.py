// https://leetcode.com/problems/sort-an-array

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge_sort(nums):
            # bottom cases: empty or list of a single element.
            if len(nums) <= 1:
                return nums

            pivot = int(len(nums) / 2)
            lft = merge_sort(nums[0:pivot])
            rgt = merge_sort(nums[pivot:])
            return merge(lft, rgt)


        def merge(left_list, right_list):
            left_cursor = right_cursor = 0
            ret = []
            while left_cursor < len(left_list) and right_cursor < len(right_list):
                  if left_list[left_cursor] < right_list[right_cursor]:
                     ret.append(left_list[left_cursor])
                     left_cursor += 1
                  else:
                     ret.append(right_list[right_cursor])
                     right_cursor += 1
    
            # append what is remained in either of the lists
            ret.extend(left_list[left_cursor:])
            ret.extend(right_list[right_cursor:])
    
            return ret
        
        return merge_sort(nums) 
            
         