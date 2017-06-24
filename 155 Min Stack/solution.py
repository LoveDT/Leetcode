class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.result = []
        self.minstack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.result.append(x)
        if len(self.minstack) and x == self.minstack[-1][0]:
            self.minstack[-1] = (x,self.minstack[-1][1]+1)
        elif len(self.minstack)==0 or x < self.minstack[-1][0]:
            self.minstack.append((x,1))

    # @return nothing
    def pop(self):
        if self.top() == self.getMin():
            if self.minstack[-1][1]>1:
                self.minstack[-1] = (self.minstack[-1][0],self.minstack[-1][1]-1)
            else:
                self.minstack.pop()
        self.result.pop()

    # @return an integer
    def top(self):
        return self.result[-1]

    # @return an integer
    def getMin(self):
        return self.minstack[-1][0]