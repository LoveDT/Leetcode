class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n<3:
            return n
        result = []
        for i in range(n+1):
            if i==0 or i==1 or i==2:
                result.append(i)
            else:
                result.append(result[i-1]+result[i-2])
        return result[-1]
        