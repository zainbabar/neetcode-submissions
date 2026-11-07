class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            # a numeric add it to stack
            if token not in ops:
                stack.append(int(token)) 
                continue
            # time to do an operation
            # the last two values on the stack are our operands 
            else:
                # the top of the stack is our most recent one 
                # so it should go second 
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    new = first + second
                elif token == "-":
                    new = first - second
                elif token == "*":
                    new = first * second
                else:
                    new = int(first /second)
                
                # now we want to update the current state of the expression 
                # for future nested operations 
                # e.g.
                # (2 + 1) * 3 = 3 * 3 = 9
                # the next op we see will use the value of the prev expression as its "first"
                stack.append(new)
        # by the end the stack should have only one value left the final expression
        return stack[0]

