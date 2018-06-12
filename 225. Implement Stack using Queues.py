from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1, self.q2 = deque(), deque()
        self._Top = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.q1: self.q1.append(x)
        else: self.q2.append(x)
        self._Top = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self._Top = None
        if self.q1:
            while len(self.q1) > 1:
                self._Top = self.q1.popleft()
                self.q2.append(self._Top)
            return self.q1.popleft()
        elif self.q2:
            while len(self.q2) > 1:
                self._Top = self.q2.popleft()
                self.q1.append(self._Top)
            return self.q2.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._Top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self._Top == None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()