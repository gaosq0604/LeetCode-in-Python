# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        result = 0
        for i, p1 in enumerate(points):
            same = 0
            counts = collections.defaultdict(lambda: 1)
            for _, p2 in enumerate(points[:i]):
                dx, dy = p2.x - p1.x, p2.y - p1.y
                if dx == 0 and dy == 0:
                    same += 1
                else:
                    slope = 'max_int' if dx == 0 else dy/dx 
                    counts[slope] += 1
            local_max = same + max(counts.values(), default=1)
            result = max(result, local_max)
        return result