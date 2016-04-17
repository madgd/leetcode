class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)
        sumN_2 = 0
        sumN_1 = 0
        sumN = 0
        for i in nums:
            sumN = max(sumN_1, sumN_2 + i)
            sumN_2 = sumN_1
            sumN_1 = sumN
        return sumN
