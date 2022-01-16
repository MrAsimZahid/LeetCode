# mrasimzahid.github.io

# method: keep a min number in stack input take a tuple (value, min_num)

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        m = val
        if self.stack:
            m = self.stack[-1][1]
            if m > val:
                m = val
        self.stack.append((val, m))

    def pop(self) -> None:
        self.stack.pop()
                          
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

    
    
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()