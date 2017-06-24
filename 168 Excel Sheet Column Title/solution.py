class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        result = ""
        tmp = n
        count = 1
        while (int((tmp-1)/26)>=1):
            count+=1
            tmp=int((tmp-1)/26)
        for i in range(count):
            result+=chr(((n-1)%26)+ord('A'))
            n = int((n-1)/26)
        return result[::-1]