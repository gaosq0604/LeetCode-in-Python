class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        from collections import deque
        v1 = deque(map(int, version1.split('.')))
        v2 = deque(map(int, version2.split('.')))
        while v1 and v2:
            t1, t2 = v1.popleft(), v2.popleft()
            if t1 > t2: return 1
            elif t1 < t2: return -1
        if v1: return 1 if max(v1) > 0 else 0
        if v2: return -1 if max(v2) > 0 else 0
        return 0