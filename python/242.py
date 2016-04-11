class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictA = {}
        dictB = {}
        for i in s:
            dictA[i] = dictA[i] + 1 if i in dictA else 1
        for i in t:
            dictB[i] = dictB[i] + 1 if i in dictB else 1
        return dictA == dictB
