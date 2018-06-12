class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            indegree[pre[0]] += 1
            graph[pre[1]].append(pre[0])
        queue = []
        res = []
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)
        while queue:
            node = queue.pop()
            res.append(node)
            for ele in graph[node]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    queue.append(ele)
        return len(res) == numCourses and res or []