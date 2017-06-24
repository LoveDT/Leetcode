class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        helper = range(1,n+1)
        k = k-1
        ans = ""
        for i in range(n-1,-1,-1):
            ind,k = divmod(k,math.factorial(i))
            ans+=str(helper[ind])
            helper.pop(ind)
        return ans