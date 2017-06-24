class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        postfix = self.infixtopostfix(s)
        return self.evalpostfix(postfix)
    def op_order(self,op):
        if op=='+' or op=='-':
            return 1
        else:
            return 2
    def infixtopostfix(self,infix):
        postfix = []
        helper = []
        tmp = ''
        for letter in infix:
            if letter == ' ':
                continue
            if ord(letter)-ord('0')>=0 and ord(letter)-ord('0')<=9:
                tmp+=letter
            else:
                if tmp!='':
                    postfix.append(tmp)
                    tmp = ''
                if len(helper)==0:
                    helper.append(letter)
                elif self.op_order(letter)>self.op_order(helper[-1]):
                    helper.append(letter)
                else:
                    while len(helper)!=0 and self.op_order(letter)<=self.op_order(helper[-1]):
                        postfix.append(helper.pop())
                    helper.append(letter)
        if tmp!='':
            postfix.append(tmp)
        while len(helper)!=0:
            postfix.append(helper.pop())
        return postfix
    def evalpostfix(self,postfix):
        numbers = []
        tmp = 0
        for element in postfix:
            if element == '+':
                tmp = numbers.pop()+numbers.pop()
                numbers.append(tmp)
            elif element == '-':
                tmp = numbers.pop()-numbers.pop()
                numbers.append(-1*tmp)
            elif element == '*':
                tmp = numbers.pop()*numbers.pop()
                numbers.append(tmp)
            elif element == '/':
                tmp = numbers[-2]/numbers[-1]
                numbers.pop()
                numbers.pop()
                numbers.append(tmp)
            else:
                numbers.append(int(element))
        if len(numbers)==1:
            result = numbers[0]
        return result
                
        