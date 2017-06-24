class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}'
    def divide(self, dividend, divisor):
        if dividend == -1*math.pow(2,31) and divisor==-1:
            return int(math.pow(2,31)-1)
        result = 0
        flag = -1
        rem = abs(dividend)
        tmp = abs(divisor)
        if rem == dividend and tmp==divisor:
            flag = 1
        elif rem!=dividend and tmp!=divisor:
            flag = 1
        while rem>=tmp:
            c = tmp
            count = 1
            while c<=rem:
                rem-=c
                result+=count
                c = c+c
                count = count+count
        return result*flag