#using bit operations
class Solution1(object):
	def hammingweight(self, n):
		"""
		:type n: int
		:trype: int
		"""
		count = 0
		while n:
			count = count + 1
			n = (n - 1) & n
		return count

#math
class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        while n!=0:
            m += n % 2
            n = n / 2
        return m

#convert to list        
class Solution3(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return list(bin(n)).count('1')

#convert to string
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return "{0:b}".format(n).count('1')
