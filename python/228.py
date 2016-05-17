class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not len(nums):
            return []
        r = []
        t = 0
        nums.append(nums[-1] + 2)
        for i in range(len(nums) - 1):
            if not nums[i + 1] == nums[i] + 1:
                if t == i:
                    r.append(str(nums[i]))
                else:
                    r.append(str(nums[t]) + '->' + str(nums[i]))
                t = i + 1
        return r
