class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n<=0:
            return 0
        result = 0
        helper = 1
        count = 0
        while n>0:
            if n%10>0:
                if n%10>1:
                    result+=helper
                else:
                    result+=count+1
            count+=(n%10)*helper
            n = int(n/10)
            result+= n*helper
            helper*=10
        return result