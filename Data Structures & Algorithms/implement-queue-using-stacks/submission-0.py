class MyQueue:

    # stack is first in last out 
    # new item goes to the top of the stack
    # but when we pop we want the bottom of the stack
    # so transfer all the items in the stack to another stack
    # which flips the stack, the last item is first and first is last
    # so pop now gives us the new last which is the old first 
    # (what we want for a queue)
    def __init__(self):
       self.input_stack = [] 
       self.output_stack= []

    def push(self, x: int) -> None:
        self.input_stack.append(x) # append onto our input stack

    def pop(self) -> int:
        # if our output (flipped) stack still has items 
        # we can just pop the most recent one 
        # since that is the oldest one pushed
        # if its empty we should transfer over from out input
        if self.output_stack:
            return self.output_stack.pop()
        # output stack is empty, flip the input stack to reverse order
        # and then return the top (bottom of input)
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())
        
        return self.output_stack.pop()

    # just a simple view so we can index, last of output 
    # or first of input is front of the queue 
    def peek(self) -> int:
        if self.output_stack:
            return self.output_stack[-1]
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())
        
        return self.output_stack[-1]
        
    def empty(self) -> bool:
        # if the input or output stacks have elements then the queue is not emptyy
        return not (bool(self.input_stack) or bool(self.output_stack))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()