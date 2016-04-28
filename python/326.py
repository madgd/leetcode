class Solution1(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
	#3486784401是3的20次幂，只能被3的整数幂次整除
        return n > 0 and not 3486784401 % n
class Solution2(object):
    def isPowerOfThree(self, n):
	#转化为log求解，如果是3的幂次，则log(n)/log(3)是整数
        return n > 0 and 3 ** round((math.log(n)/math.log(3))) == n
