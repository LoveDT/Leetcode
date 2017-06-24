class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        for i in range(32):
            if (n&1)==1:
                result+=1
            n>>=1
        return result