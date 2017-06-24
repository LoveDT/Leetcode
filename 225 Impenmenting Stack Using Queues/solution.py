class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.result = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.result.append(x)
        

    # @return nothing
    def pop(self):
        self.result.pop()

    # @return an integer
    def top(self):
        return self.result[-1]
        

    # @return an boolean
    def empty(self):
        return True if len(self.result)==0 else False
        