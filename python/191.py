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
