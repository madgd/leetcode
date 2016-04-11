class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i + j < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                j = j + 1
            else:
                i = i + 1
