class MinStack:

    def __init__(self):
        self.min=[]

    def push(self, val: int) -> None:
        self.min.append(val)

    def pop(self) -> None:
        a=len(self.min)
        self.min=self.min[:a-1]
        return self.min
        

    def top(self) -> int:
        top = self.min[0]
        
        for i in self.min :
            if i > top :
                top = i
        return top

    def getMin(self) -> int:
        mini = self.min[0]
        for i in self.min :
            if i < mini :
                mini = i
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()