class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        table  = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        result = 0
        if len(s)==1:
            return table[s[0]]
        for i in range(len(s)-1):
            if table[s[i]]<table[s[i+1]]:
                result-=table[s[i]]
            else:
                result+=table[s[i]]
        result+=table[s[-1]]
        return result
        
        