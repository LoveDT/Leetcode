class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        result = 0
        while (n!=1):
            n,result = divmod(n,2)
            if result ==1:
                return False
        return True
        