class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i, ele in enumerate(tokens):
            if ele in '+-*/':
                v2 = stack.pop()
                v1 = stack.pop()
                if ele == '+': res = v1 + v2
                if ele == '-': res = v1 - v2
                if ele == '*': res = v1 * v2
                if ele == '/': res = int(v1 / v2)
                stack.append(res)
            else:
                stack.append(int(ele))
        return stack[-1]