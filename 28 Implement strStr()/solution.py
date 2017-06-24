class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        length, inlen = len(haystack), len(needle)
        if inlen == 0:
            return 0
        if length == 0:
            return -1
        h,n,result = 0,0,0
        while h<length:
            if haystack[h] == needle[n]:
                result = h
                while n<inlen and h<length and haystack[h] == needle[n]:
                    h+=1
                    n+=1
                if n == inlen:
                    return result
                elif h == length:
                    return -1
                else:
                    h -= (n-1)
                    n = 0
            else:
                h += 1
        return -1
                    
            
        