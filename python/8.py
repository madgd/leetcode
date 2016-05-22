class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #排除几种情况
        if (not str) or str == '-' or str == '+':
            return 0

        #去除输入字符串前导空格
        while str[0] == ' ':
            str = str[1:]

        #数字列表
        numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        num = 0
        m = 0
        if str[0] == '-' or str[0] == '+':
            m = 1
        #遍历并计算
        for i in str[m:]:
            if not i in numList:
                break
            num = num * 10 + ord(i) - 48
        #如果是负数
        if str[0] == '-':
                num = -num

        #超出范围截断数据
        if num >= 1<<31:
            num = (1<<31)-1
        elif num < -1<<31:
            num = - 1<<31
        return num
