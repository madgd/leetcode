class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #当前状态决定于前两阶状态
        #若偷最后一家，则倒数第二家不能偷，若此时达到最大，则最大为sumN_2+i
        #若不偷最后一家，则一定偷倒数第二家，若此时达到最大，则最大为sumN_1
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
