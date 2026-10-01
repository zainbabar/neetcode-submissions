class Solution:
    def isValid(self, s: str) -> bool:
        # append opening brackets to top of a stack
        # if we hit a closing bracket and opening bracket is not
        # the top of stack
        # issue, should be most recetnyl closing
        stack = []
        pairs = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if c in pairs.values(): # opening bracket add to stack
                stack.append(c)
            if c in pairs.keys(): # closing bracket
                if len(stack) < 1: # no opening bracket in stack
                    return False
                elif stack[-1] != pairs[c]: # no CORRESPONDING closing bracket
                    return False
                else: # corresponding, pop it
                    stack.pop()
          
        if len(stack) > 0: # forgot to close out a bracket
            return False
        else:
            return True 
            
                