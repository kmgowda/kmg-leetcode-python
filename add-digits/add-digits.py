// https://leetcode.com/problems/add-digits

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num % 9 if num % 9 or not num else 9