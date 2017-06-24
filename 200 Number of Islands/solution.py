class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    result += 1
                    self.removeIsland(i, j, grid)
        return result
    
    def removeIsland(self, row, col, grid):
        m, n = len(grid), len(grid[0])
        grid[row][col] = "0"
        if row - 1 >= 0 and grid[row - 1][col] == "1":
            self.removeIsland(row - 1, col, grid)
        if row + 1 < m and grid[row + 1][col] == "1":
            self.removeIsland(row + 1, col, grid)
        if col - 1 >= 0 and grid[row][col - 1] == "1":
            self.removeIsland(row, col - 1, grid)
        if col + 1 < n and grid[row][col + 1] == "1":
            self.removeIsland(row, col + 1, grid)