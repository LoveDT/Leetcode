class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not len(matrix):
            return 0
        m = len(matrix)
        n = len(matrix[0])
        result = [[0 for i in range(n)] for j in range(m)]
        maxnum = result[0][0]
        for i in range(n):
            if matrix[0][i] == '1':
                result[0][i] = 1
                maxnum = 1
            else:
                result[0][i] = 0
        for j in range(m):
            if matrix[j][0] == '1':
                result[j][0] = 1
                maxnum = 1
            else:
                result[j][0] = 0
        for j in range(1,m):
            for i in range(1,n):
                if matrix[j][i] == '1':
                    left = result[j][i-1]
                    up = result[j-1][i]
                    upleft = result[j-1][i-1]
                    if left == up and up == upleft and up:
                        result[j][i] = left + 1
                        maxnum = max(maxnum, result[j][i])
                    elif left * up * upleft > 0:
                        result[j][i] = min(left, up, upleft) + 1
                    else:
                        result[j][i] = 1
                else:
                    result[j][i] = 0
        return maxnum * maxnum
        