class Solution1(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #类型转化法
        return str(bin(int(a, 2) + int(b, 2)))[2:]

class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lenga = len(a)
        lengb = len(b)
        leng= max(lenga, lengb)
        up = '0'
        A = '0'
        B = '0'
        res = ''
        for i in range(leng):
            if i >= lenga:
                A = '0'
            else:
                A = a[-i-1]
            if i >= lengb:
                B = '0'
            else:
                B = b[-i-1]

            if A == B:
                if up == '0':
                    res = '0' + res
                else:
                    res = '1' + res
                if '0' in (A,B):
                    up = '0'
                else:
                    up = '1'
            else:
                if up == '1':
                    res = '0' + res
                    up = '1'
                else:
                    res = '1' + res

                    if '0' in (A,B):
                        up = '0'
                    else:
                        up = '1'

        if up == '1':
            res = '1' + res

        return res

class Solution3(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #递归方法
        if not a:
            return b
        if not b:
            return a
        if a[-1] == b[-1] == '0':
            return self.addBinary(a[:-1:], b[:-1:]) + '0'
        elif a[-1] == b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1:], b[:-1:]), '1') + '0'
        else:
            return self.addBinary(a[:-1:], b[:-1:]) + '1'
