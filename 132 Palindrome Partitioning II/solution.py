class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        result = [i - 1 for i in range(len(s) + 1)]
        result_data = self.preparation(s)
        for end in range(1, len(result)):
            for start in range(end):
                if result_data[start][end - 1]:
                    result[end] = min(result[end], result[start] + 1)
        return result[-1]
        
    
    def preparation(self, s):
        length = len(s)
        result_data = [[False for i in range(length)] for j in range(length)]
        result_data[-1][-1] = True
        for i in range(length - 1):
            result_data[i][i] = True
            if s[i] == s[i + 1]:
                result_data[i][i + 1] = True
        for inc in range(2, length):
            for start in range(length - inc):
                if s[start] == s[start + inc] and result_data[start + 1][start + inc - 1]:
                    result_data[start][start+inc] = True
        return result_data
            