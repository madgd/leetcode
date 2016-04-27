class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = list(s)
        vowelsList = ['a','e','i','o','u','A','E','I','O','U']
        leng = len(s)
        i = 0
        j = -1
        while i - j <  leng:
            if sList[i] in vowelsList and sList[j] in vowelsList:
                sList[i],sList[j] = sList[j],sList[i]
                i += 1
                j += -1
            else:
                if sList[i] not in vowelsList:
                    i += 1
                if sList[j] not in vowelsList:
                    j += -1
        return ''.join(sList)
