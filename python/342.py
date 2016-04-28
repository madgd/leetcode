class Solution1(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #不是0,是二的幂(二进制只有第一位是1),二进制长度为奇数
        return bool(num > 0 and (not num & (num - 1)) and len(bin(num)) & 1)
class Solution2(object):
    def isPowerOfFour(self, num):
        #4的幂次减1必然能整除3
        return bool(num > 0 and (not num & (num - 1)) and not (num - 1) % 3)
class Solution(object):
    def isPowerOfFour(self, num):
        #位运算
        return bool(num > 0 and (not num & (num - 1)) and num & 0x55555555)
