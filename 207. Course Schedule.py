class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            indegree[pre[0]] += 1
            graph[pre[1]].append(pre[0])
        queue = []
        count = 0
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)
                count += 1
        while queue:
            node = queue.pop()
            for ele in graph[node]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    queue.append(ele)
                    count += 1
        return count == numCourses