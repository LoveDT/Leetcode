class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1=="0" or num2=="0":
            return "0";
        num3 = num1[::-1]
        num4 = num2[::-1]
        arr = [0 for i in range(len(num3)+len(num4))]
        for i in range(len(num3)):
            for j in range(len(num4)):
                arr[i+j]+=int(num3[i])*int(num4[j])
        ans = []
        for i in range(len(arr)):
            flag,digit = divmod(arr[i],10)
            if i<len(arr)-1:
                arr[i+1]+=flag
            ans.append(str(digit))
        ans = ans[::-1]
        while ans[0]=='0':
            del ans[0]
        return ''.join(ans)
        