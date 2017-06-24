class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        result = 1
        count = 1
        power = abs(n)
        helper = x
        while (power>=count):
            tmp = count
            helper = x
            while(tmp<=power):
                result*=helper
                helper*=helper
                power-=tmp
                tmp+=tmp
        return result if n==abs(n) else 1/result
                
        