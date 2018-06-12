from collections import deque
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        post = deque()
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s)-1 and s[i+1].isdigit():
                    i += 1
                post.append(int(s[start: i+1]))
            elif s[i] == '(':
                stack.append(s[i])
            elif s[i] in '+-':
                while stack and stack[-1] != '(':
                    post.append(stack.pop())
                stack.append(s[i])
            elif s[i] == ')':
                while stack[-1] != '(':
                    post.append(stack.pop())
                stack.pop()
            i += 1
        while stack:
            post.append(stack.pop())
        while post:
            item = post.popleft()
            if item in ['+', '-']:
                t2 = stack.pop()
                t1 = stack.pop()
                stack.append(t1+t2 if item == '+' else t1-t2)
            else:
                stack.append(item)
        return stack[0]