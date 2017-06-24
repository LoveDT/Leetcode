class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0:
            return 0
        m = len(matrix)
        cur = matrix[0]
        result = self.findCurrentMaximum(cur)
        for i in range(1,m):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    matrix[i][j] = str(1 + int(cur[j]))
            cur = matrix[i]
            result = max(result, self.findCurrentMaximum(cur))
        return result
    
    def findCurrentMaximum(self, string):
        helper = []
        length = len(string)
        result = 0
        for i in range(length + 1):
            edge = int(string[i]) if i < length else -1
            while helper and int(string[helper[-1]]) > edge:
                height = int(string[helper.pop()])
                width = i - helper[-1] - 1 if helper else i
                result = max(result, height * width)
            helper.append(i)
        return result