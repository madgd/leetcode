class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last=None
        rt=0
        for x in nums:
            if x!=last:
                last=x
                nums[rt]=x
                rt+=1
        #for i in range(rt,len(nums)):
            #nums.pop()
        return rt

class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for m in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i = i + 1

        return i + 1
