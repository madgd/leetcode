class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #筛法
        if n < 2:
            return 0
        nums = [True] * n
        nums[0] = nums[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if nums[i]:
                nums[i * i: n: i] = [False] * len(nums[i * i: n: i])

        return nums.count(True
