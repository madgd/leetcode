class Solution1(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1] * (rowIndex + 1)
        comb_next = lambda x, m, n: x * (m - n + 1) // n
        for n in range(1, rowIndex // 2 + 1):
            ret[n] = ret[-n-1] = comb_next(ret[n-1], rowIndex, n)
        return ret

class Solution2(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = []
        for i in range(rowIndex + 1):
            t = 1
            for m in range(i + 1):
                if m == i:
                    row.append(1)
                elif m != 0:
                    row[m], t = row[m] + t, row[m]

        return row
