class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or len(matrix) == 0:
            return None
        m = len(matrix)
        n = len(matrix[0])
        self.result = [[0 for i in range(n)] for i in range(m)]
        self.result[0][0] = matrix[0][0]
        for i in range(1, n):
            self.result[0][i] = self.result[0][i - 1] + matrix[0][i]
        for i in range(1, m):
            self.result[i][0] = self.result[i - 1][0] + matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                self.result[i][j] = matrix[i][j] + self.result[i][j - 1] + self.result[i - 1][j] - self.result[i - 1][j - 1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.result[row2][col2]
        elif row1 == 0:
            return self.result[row2][col2] - self.result[row2][col1 - 1]
        elif col1 == 0:
            return self.result[row2][col2] - self.result[row1 - 1][col2]
        else:
            return self.result[row2][col2] + self.result[row1 - 1][col1 - 1] - self.result[row2][col1 - 1] - self.result[row1 - 1][col2]
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)