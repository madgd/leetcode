class Solution1(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #自顶向下递推路径
        sumList = [triangle[0][0]]
        for i in range(1, len(triangle)):
            sumList.append(sumList[i - 1] + triangle[i][i])
            for j in range(i-1, 0, -1):
                sumList[j] = min(sumList[j], sumList[j - 1]) + triangle[i][j]
            sumList[0] += triangle[i][0]
        return min(sumList)
