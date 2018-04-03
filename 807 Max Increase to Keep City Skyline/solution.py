class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return -1
        horizontal_max = [0] * len(grid[0])
        vertical_max = []
        for i in range(len(grid)):
            cur_max = 0
            for j in range(len(grid[i])):
                cur_element = grid[i][j]
                if  cur_element > cur_max:
                    cur_max = cur_element
                if cur_element > horizontal_max[j]:
                    horizontal_max[j] = cur_element
            vertical_max.append(cur_max)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result += min(horizontal_max[j], vertical_max[i]) - grid[i][j]
        return result