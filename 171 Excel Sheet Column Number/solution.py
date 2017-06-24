class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        length = len(s)
        result = 0
        for i in range(length):
            result = result*26+(ord(s[i])-ord('A')+1)
        return result