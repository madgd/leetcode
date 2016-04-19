class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(numRows):
            row = []
            for m in range(i + 1):
                if m == 0 or m == i:
                    row.append(1)
                else:
                    row.append(nums[i-1][m-1] + nums[i-1][m])
            nums.append(row)
        return nums

