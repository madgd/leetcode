class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numsList=[
        ['','I','II','III','IV','V','VI','VII','VIII','IX'],
        ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
        ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
        ['','M','MM','MMM']]
        s = ''
        i = 0
        while num:
            j,num = num % 10, num / 10
            s = numsList[i][j] + s
            i += 1
        return s
class Solution2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        I = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        M = ['','M','MM','MMM']
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[(num%10)]
