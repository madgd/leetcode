class Solution1(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        checkDict = {}
        for i in range(len(nums)):
            if nums[i] in checkDict:
                if i - checkDict[nums[i]] <= k:
                    return True
            checkDict[nums[i]] = i
        return False

class Solution2(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0:
            return False
        if k > len(nums):
            k = len(nums)
        checkSet = set(nums[:k:])
        if len(checkSet) < k:
            return True
        for i in range(k, len(nums)):
            if nums[i] in checkSet:
                return True
            else:
                checkSet.discard(nums[i - k])
                checkSet.add(nums[i])
        return False
