class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Manacher算法
        #将原字符串用没有在其中出现的字符(这里是'#')相隔,可以统一奇偶
        #对新的字符串,设立辅助数组, 每一位代表以当前对应的字符为中心的回文字符串向后延伸的长度(包含当前为)

        sMan = '$' + '#' + ''.join([i + '#' for i in s])
        leng = len(sMan)
        sList = [0] * leng
        #mx代表当前向右延伸的最远段,imx为对应的中心id
        mx = 1
        imx = 1

        #计算辅助数组sList的值,对第i为,则i前面的位的值均已经求出
        for i in xrange(1, leng):
            #如果i再最右延伸位之内,则j为i关于最右延伸位的回文字符串中点imx对称的点,位于mx内的部分完全对称
            if i < mx:
                j = imx - (i - imx)
                #如果sList[j]的值较大,则取mx-i为初始值
                sList[i] = min(mx - i, sList[j])
            #如果当前计算位大于最右延伸位,那么初始值为1
            else:
                sList[i] = 1

            #在刚才的基础上继续向两段匹配
            while i + sList[i] < leng and sMan[i + sList[i]] == sMan[i - sList[i]]:
                sList[i] += 1

            #更新最右延伸范围
            if sList[i] + i > mx:
                mx = sList[i] + i
                imx = i

        #这里mx代表辅助数组中的最大值,imx为对应的中心id.需要取出最大值和对应id
        mx = 0
        imx = 0
        for i in xrange(1, leng):
            if sList[i] > mx:
                mx = sList[i]
                imx = i

        #return sMan
        return s[(imx - mx) // 2 : (imx + mx - 1) // 2]
