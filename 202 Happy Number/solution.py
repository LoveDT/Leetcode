class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        resultset = set()
        while n!=1 and n not in resultset:
            resultset.add(n)
            happy = 0
            while n:
                m,digit = divmod(n,10)
                happy+=digit*digit
                n = m
            n = happy
        return n==1
        