class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return -1
        if n < 7:
            return n
        uglynumbers = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(n - 1):
            cand2, cand3, cand5 = uglynumbers[i2] * 2, uglynumbers[i3] * 3, uglynumbers[i5] * 5
            cand = min(cand2, cand3, cand5)
            uglynumbers.append(cand)
            if cand == cand2:
                i2 += 1
            if cand == cand3:
                i3 += 1
            if cand == cand5:
                i5 += 1
        return uglynumbers[-1]
        