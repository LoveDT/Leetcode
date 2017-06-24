class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        result = -1
        flag = 1
        count = 0
        strhelper = ""
        for char in str:
            if char=='-' or char=='+':
                strhelper+=char
            elif ord(char)-ord('0')>=0 and ord(char)-ord('0')<=9:
                strhelper+=char
            elif ord(char)-ord('0')>=0 and len(strhelper)==0:
                return 0
            elif len(strhelper):
                break
        for char in strhelper:
            if char=='-' or char=='+':
                count+=1
                if char=='-':
                    flag=  -1
            if count>1:
                return 0
            helper = ord(char)-ord('0')
            if helper>=0 and helper<=9:
                if result<0:
                    result = helper
                else:
                    result = result*10+helper
            elif result>=0:
                break
        if result>math.pow(2,31) and flag == -1:
            return int(math.pow(2,31)*flag)
        elif result>math.pow(2,31)-1 and flag == 1:
            return int(math.pow(2,31)-1)
        return result*flag if result>=0 else 0
        
        