class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #转化为set，取交集
        return list(set(nums1) & set(nums2))

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #用dict记录
        Dict = {}
        res = []
        for i in nums1:
            if i in Dict:
                pass
            else:
                Dict[i] = 0
        for j in nums2:
            if j in Dict and Dict[j] == 0:
                res.append(j)
                Dict[j] = 1

        return res
