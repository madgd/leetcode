class Solution1(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1:
            return [1, 0]
        else:
            return self.plusOne(digits[:-1]) + [0]

class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        l =list()
        for i in digits:
            s = s + str(i)
        s = str(int(s) + 1)
        for i in s:
            l.append(int(i))
        return l
