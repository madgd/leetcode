class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while not num % 2:
            num = num / 2            
        while not num % 3:
            num = num / 3
        while not num % 5:
            num = num / 5            
        if num == 1:
            return True
        else:
            return False
