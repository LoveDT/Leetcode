class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result = []
        if numRows==0:
            return result
        helper = [1]
        result.append(helper)
        for i in range(numRows-1):
            tmp = helper
            helper = [1]
            for j in range(i):
                helper.append(tmp[j]+tmp[j+1])
            helper.append(1)
            result.append(helper)
        return result