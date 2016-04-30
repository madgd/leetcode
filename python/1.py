class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    	numsDict = {}
    	for i in range(len(nums)):
    		numsDict[target - nums[i]] = i
    	for i in range(len(nums)):
    		if nums[i] in numsDict and i != numsDict[nums[i]]:
    			return [i,numsDict[nums[i]]]
