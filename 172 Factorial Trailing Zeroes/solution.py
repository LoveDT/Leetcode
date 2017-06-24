class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        result,count = 0,0
        tmp = n
        while (tmp/5>=1):
            count+=1
            tmp = tmp/5
        for i in range(count):
            result+=int(n/math.pow(5,i+1))
        return result