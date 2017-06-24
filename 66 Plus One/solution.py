class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        digits.reverse()
        nxt = 0
        nxt,digits[0] = divmod(digits[0]+1,10)
        for i in range(1,len(digits)):
            tmp = nxt
            nxt,digits[i] = divmod(digits[i]+tmp,10)
        if nxt==1:
            digits.append(1)
        digits.reverse()
        return digits
        