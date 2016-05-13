class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dict记录
        dictNum = {}
        for i in nums:
            if not dictNum.has_key(i):
                dictNum[i] = True
            else:
                dictNum.pop(i)
        return dictNum.keys()[0]

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #set求和
        return (2*sum(set(nums))-sum(nums))

class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #与自身异或为0,与0异或为自身
        r = 0
        for i in nums:
            r = r ^ i
        return r
