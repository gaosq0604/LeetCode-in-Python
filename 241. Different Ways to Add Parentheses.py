class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def axb(a, x, b):
            if x == "+":
                return a + b

            if x == "-":
                return a - b

            if x == "*":
                return a * b

        source = []
        origin = ""
        for s in input:
            if s == "+" or s == "-" or s == "*":
                source.append(int(origin))
                source.append(s)
                origin = ""
            else:
                origin+=s
        source.append(int(origin))

        def func(A):

            if len(A) == 1:
                return A
            if len(A) == 3:
                return [axb(*A)]

            result = []
            for exp in range(1, len(A), 2):
                x = A[:exp]
                y = A[exp+1:]
                for i in func(x):
                    for j in func(y):
                        result.append(axb(i, A[exp], j))
            return result

        return func(source)