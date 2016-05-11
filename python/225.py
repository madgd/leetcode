class Stack1(object):
    #两个队列实现，O(n)pop和top
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.queue1:
            while len(self.queue1) > 1:
                q = self.queue1.pop(0)
                self.queue2.append(q)
            self.queue1.pop(0)
        else:
            while len(self.queue2) > 1:
                q = self.queue2.pop(0)
                self.queue1.append(q)
            self.queue2.pop(0)

    def top(self):
        """
        :rtype: int
        """
        if self.queue1:
            while self.queue1:
                q = self.queue1.pop(0)
                self.queue2.append(q)
        else:
            while self.queue2:
                q = self.queue2.pop(0)
                self.queue1.append(q)
        return q

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.queue1 or self.queue2)

class Stack2(object):
    #O(n) push,其他O(1)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        for i in xrange(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue
