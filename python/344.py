class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(reversed(list(s)))
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
