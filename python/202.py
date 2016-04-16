class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 4:
            return False
        else:
            return self.isHappy(sum(int(i)**2 for i in str(n)))
class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        past = set()			
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in past:
                return False
            past.add(n)
        return True
