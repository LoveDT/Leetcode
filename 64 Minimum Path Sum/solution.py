class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        helper = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    helper[i][j] = grid[i][j]
                elif i == 0:
                    helper[i][j] = helper[i][j - 1] + grid[i][j]
                elif j == 0:
                    helper[i][j] = helper[i - 1][j] + grid[i][j]
                else:
                    helper[i][j] = min(helper[i][j - 1], helper[i - 1][j]) + grid[i][j]
        return helper[-1][-1]
        