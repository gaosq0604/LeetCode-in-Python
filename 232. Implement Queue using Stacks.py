class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1, self.s2 = [], []
        self.top = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.s1: self.top = x
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        res = self.s2.pop()
        self.top = self.s2[-1] if self.s2 else None
        while self.s2:
            self.s1.append(self.s2.pop())
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.top

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.top


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()