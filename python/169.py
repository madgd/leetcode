class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = []
        for i in nums:
            if len(n) == 0:
                n.append(i)
            elif i != n[-1]:
                n.pop()
            else:
                n.append(i)
        return n.pop()

class Solution1_improve(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = nums[0]
        count = 0
        for i in nums:
            if count == 0:
                n = i
                count = 1
            elif i == n:
                count = count + 1
            else:
                count = count - 1
        return n

class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]

class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        checkDict = {}
        leng = len(nums)//2
        for i in nums:
            if not i in checkDict:
                checkDict[i] = 1
            else:
                checkDict[i] = checkDict[i] + 1
            if checkDict[i] > leng:
                return i
