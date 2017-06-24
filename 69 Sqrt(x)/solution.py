class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x==0:
            return 0
        tmp,helper = 1,0
        result,getin = 0,0
        while x>=(result+tmp)*(result+tmp):
            helper = tmp
            while x>=(result+helper)*(result+helper):
                getin = helper
                helper*=2
            result+=getin
        return result