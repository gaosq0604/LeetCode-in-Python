class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        r, n = 0, len(gas)
        min_ = float('inf')
        for i in range(n):
            r += gas[i]-cost[i]
            if r < min_:
                min_, k = r, i
        return (k+1)%n