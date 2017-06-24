from pythonds.basic.stack import Stack
def baseConverter(number,base):
	remstack = Stack()
	while number>0:
		rem = number%base
		remstack.push(rem)
		number = number//base

n = 1
print bin(n)
tmp = list(bin(n))
tmp.reverse
print tmp
cur = "".join(tmp)
result = 0
for digit in tmp:
	print int(digit)
	result = result*2+int(digit)
print result

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rem = n
        tmp = []
        for i in range(32):
            ans = 0
            (tmp_rem,ans)=divmod(rem,2)
            rem = tmp_rem
            tmp.append(ans)
        result = str("".join(tmp))
        result = int(result,2)
        return result