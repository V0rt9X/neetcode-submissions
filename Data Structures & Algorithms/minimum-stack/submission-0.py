class MinStack:

    def __init__(self):
        self.stack = [] # Default stack
        self.minStack = [] # Stack for store min value from main stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # Validation if val lower than last min val in minStack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # Returning top value from stack

    def getMin(self) -> int:
        return self.minStack[-1] # Returning top value from minStack whitch is min value in stack
        
