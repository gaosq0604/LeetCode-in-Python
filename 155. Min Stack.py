class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curmin = self.getMin()
        if curmin == None or x < curmin: curmin = x
        self.q.append((x, curmin))

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.q: return None
        return self.q[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.q: return None
        return self.q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()