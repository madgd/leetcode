class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        leng = len(nums1) + len(nums2)
        if leng % 2:
            return self.findKth(nums1, nums2, leng // 2)
        else:
            return (self.findKth(nums1, nums2, leng // 2) + self.findKth(nums1, nums2, leng // 2 - 1)) / 2.0

    #该函数找到两个有序序列中第k大的数，基本思想类似二分法。
    #
    def findKth(self, A, B, k):
        lengA = len(A)
        lengB = len(B)
        if not lengA:
            return B[k]
        if not lengB:
            return A[k]
        ia = lengA // 2
        ib = lengB // 2
        ma = A[ia]
        mb = B[ib]

        #如果两数组的各一半的和小于k，意味着k在后半部分
        if ia + ib < k:
            #如果ma比较大，那第k大的数不可能在b的前半部分
            if ma > mb:
                return self.findKth(A, B[ib+1:], k - ib -1)
            else:
                return self.findKth(A[ia+1:], B, k - ia -1)
        #如果如果两数组的各一半的和大于k，意味着k在前半部分
        else:
            #如果ma比较大，那第k大的数不可能在a的后半部分
            if ma > mb:
                return self.findKth(A[:ia], B, k)
            else:
                return self.findKth(A, B[:ib], k)
