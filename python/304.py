class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        #按顺序递推求出以从(0,0)到（i,j)的和，初始化的时间复杂度为O(m+n)
        self.sumsMatrix = matrix
        lengI = len(matrix)
        #如果输入为空数组
        if not lengI:
            return
        lengJ = len(matrix[0])
        for i in xrange(1, lengI):
            self.sumsMatrix[i][0] += self.sumsMatrix[i-1][0]
        for j in xrange(1, lengJ):
            self.sumsMatrix[0][j] += self.sumsMatrix[0][j-1]
        for i in xrange(1, lengI):
            for j in xrange(1, lengJ):
                self.sumsMatrix[i][j] += (self.sumsMatrix[i-1][j] + self.sumsMatrix[i][j-1] - self.sumsMatrix[i-1][j-1])

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        #计算出(row1, col1)到(row2, col2)的和
        sum = self.sumsMatrix[row2][col2]
        sum -= self.sumsMatrix[row1-1][col2] if row1 else 0
        sum -= self.sumsMatrix[row2][col1-1] if col1 else 0
        sum += self.sumsMatrix[row1-1][col1-1] if row1 and col1 else 0
        return sum
