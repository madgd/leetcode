class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #长度不足收益为0
        leng = len(prices)
        if leng <= 1:
            return 0
        i = 0
        #找到第一次可以赚钱的位置
        while i < leng - 1 and prices[i] >= prices[i + 1]:
            i += 1
        if i == leng - 1:
            return 0
        #初始化Max为当前最大收益对应的最大卖出价格，Min是卖出价格后出现的最小买入价格
        #res是当前可能最大收益
        Max = prices[i + 1]
        Min = Max
        res = Max - prices[i]
        
        i += 2
        #转移到下一个状态
        while i < leng:
            #比之前的最大收益对应的最大值大，更新最大值和最大收益
            if prices[i] > Max:
                res += prices[i] - Max
                Max = prices[i]
            #新的值减去当前最小值大于最大收益，更新最大值和最大收益
            if prices[i] - Min > res:
                res = prices[i] - Min
                Max = prices[i]
            #新的值比当前最小值小，更新最小值
            if prices[i] < Min:
                Min = prices[i]
            i += 1
        return res
