class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #检验每一组9个元素中是否有重复元素
        def isValid(str):
            checkDict = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for i in str:
                if i != '.':
                    checkDict[i] += 1
                    if checkDict[i] > 1:
                        return False
            return True

        #遍历9行
        for i in board:
            if not isValid(i):
                return False
        #遍历9列
        for i in xrange(9):
            checkStr = ''
            for j in xrange(9):
                checkStr += board[j][i]
            if not isValid(checkStr):
                return False
        #遍历9块
        for i in xrange(3):
            for j in xrange(3):
                checkStr = ''
                for k in xrange(3):
                    checkStr += ''.join(board[j*3 + k][i*3:i*3+3])
                if not isValid(checkStr):
                    return False

        return True
