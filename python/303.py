class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #从第一位开始的和数组，O(n)
        self.sums = nums
        for i in xrange(1, len(nums)):
            self.sums[i] += self.sums[i - 1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #两和相减
        return self.sums[j] - self.sums[i-1] if i > 0 else self.sums[j]
