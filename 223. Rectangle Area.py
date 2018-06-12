class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x1, x2, x3 = C - A, G - E, max(C, G) - min(A, E) 
        y1, y2, y3 = D - B, H - F, max(D, H) - min(B, F)
        intrs = (x1 + x2 - x3) * (y1 + y2 - y3) if x3 < x1 + x2 and y3 < y1 + y2 else 0
        return x1 * y1 + x2 * y2 - intrs