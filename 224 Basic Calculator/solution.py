class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        postfix = self.infixtopostfix(s)
        return self.evalpostfix(postfix)
    def infixtopostfix(self,infix):
        postfix = []
        helper = []
        tmp = ''
        for letter in infix:
            if letter=='(':
                helper.append(letter)
            elif ord(letter)-ord('0')<=9 and ord(letter)-ord('0')>=0:
                tmp+=letter
            else:
                if tmp!='':
                    postfix.append(tmp)
                    tmp = ''
                if letter=='-' or letter == '+':
                    if len(helper)==0 or helper[-1]=='(':
                        helper.append(letter)
                    else:
                        while len(helper)!=0 and helper[-1]!='(':
                            postfix.append(helper.pop())
                        helper.append(letter)
                elif letter==')':
                    while helper[-1]!='(':
                        postfix.append(helper.pop())
                    helper.pop()
        if tmp!='':
            postfix.append(tmp)
        while len(helper)!=0:
            postfix.append(helper.pop())
        return postfix
    def evalpostfix(self,postfix):
        result = 0
        numbers = []
        for letter in postfix:
            if letter == '+':
                tmp = numbers.pop()+numbers.pop()
                numbers.append(tmp)
            elif letter == '-':
                tmp = numbers.pop()-numbers.pop()
                numbers.append(-1*tmp)
            else:
                numbers.append(int(letter))
        if len(numbers) ==1:
            result = numbers[0]
        return result
        