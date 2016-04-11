class Solution1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num >= 10:
            if num % 9 == 0:
                return 9
            return num % 9
        else:
            return num
class Solution2(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
