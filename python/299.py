class Solution1(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
        return '%dA%dB' % (bulls, both - bulls)

class Solution2(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secretList = list(secret)
        guessList = list(guess)
        A = 0
        i = 0
        leng = len(secretList)
        while i < leng:
            if secretList[i] == guessList[i]:
                A = A + 1
                del secretList[i]
                del guessList[i]
                leng = leng - 1
            else:
                i = i + 1
                
        B = 0
        for i in secretList:
            if i in guessList:
                B = B + 1
                guessList.remove(i)
        return "%sA%sB"%(A,B)
