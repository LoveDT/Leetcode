class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        number = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        result = ''
        for i in range(len(value)):
            while num>=value[i]:
                num-=value[i]
                result+=number[i]
        return result
        