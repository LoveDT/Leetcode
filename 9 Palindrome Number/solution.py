class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        result = 0
        tmp = x
        while (tmp>0):
            tmp,rem = divmod(tmp,10)
            result = result*10+rem
        return result==x
        