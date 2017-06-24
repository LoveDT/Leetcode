class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        result = [1]
        for i in range(rowIndex):
            tmp = result
            result = [1]
            for j in range(i):
                result.append(tmp[j]+tmp[j+1])
            result.append(1)
        return result