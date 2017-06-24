class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        result = [True]*max(2,n)
        result[0] = False
        result[1] = False
        init = 2
        while init*init<n:
            if result[init]:
                mark = init*init
                while mark<n:
                    result[mark] = False
                    mark+=init
            init+=1
        return sum(result)
        