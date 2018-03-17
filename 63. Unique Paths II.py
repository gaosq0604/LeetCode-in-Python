class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        r,c=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0
        obstacleGrid[0][0]=1
        for i in range(1,r):
            obstacleGrid[i][0]=obstacleGrid[i-1][0] if not obstacleGrid[i][0] else 0
        for i in range(1,c):
            obstacleGrid[0][i]=obstacleGrid[0][i-1] if not obstacleGrid[0][i] else 0
        for i in range(1,r):
            for j in range(1,c):
                obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1] if not obstacleGrid[i][j] else 0
        return obstacleGrid[-1][-1]