class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not len(matrix):
            return False
        n,m = len(matrix)-1,len(matrix[0])
        l = 0
        while n>=0 and l<m:
            helper = matrix[n][l]
            if helper==target:
                return True
            elif helper<target:
                l+=1
            else:
                n-=1
        return False
        