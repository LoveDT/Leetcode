class Solution:
    # @return an integer
    def reverse(self, x):
        result = 0
        res = 0
        tmp = abs(x)
        while (tmp!=0):
            (tmp,res) = divmod(tmp,10)
            result = result*10+res
        if result>math.pow(2,31)-1 or result<-1*math.pow(2,31):
            return 0
        return result if x>0 else -1*result
        