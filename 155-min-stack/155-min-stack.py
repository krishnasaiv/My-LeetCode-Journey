class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.minElement = float('inf')
        self.data = list()
        self.minElements = list()
        

    def push(self, val: int) -> None:
        if len(self.data) == 0:
            self.minElements.append(val)
        else:
            self.minElements.append(min(self.minElements[-1], val))
        self.data.append(val)
        

    def pop(self) -> None:
        self.data.pop()
        self.minElements.pop()

    def top(self) -> int:
        return(self.data[-1])

    def getMin(self) -> int:
        return(self.minElements[-1])
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()