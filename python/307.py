class NumArray(object):
    #树状数组法
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.s = [0] * len(nums)
        for i in xrange(1, len(nums) + 1):
            for j in xrange(i - self.lowbit(i) + 1, i+1):
                self.s[i-1] += nums[j-1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        leng = len(self.s)
        i += 1
        while i <= leng:
            self.s[i-1] += diff
            i += self.lowbit(i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sumJ = 0
        sumI = 0
        j = j+1
        while j > 0:
            sumJ += self.s[j-1]
            j -= self.lowbit(j)
        if i == 0:
            return sumJ
        while i > 0:
            sumI += self.s[i-1]
            i -= self.lowbit(i)
        return sumJ - sumI

    def lowbit(self, k):
        return k & -k
