class Solution:
    def isValid(self, s: str) -> bool:
        # append opening brackets to top of a stack
        # if we hit a closing bracket and opening bracket is not
        # the top of stack
        # issue, should be most recetnyl closing
        stack = []
        closing = ['}', ')', ']']
        for c in s:
            if c == '{' or c == '[' or c == '(': # add an opening 
                stack.append(c)
            # check if its closing, and if it dont match
            if c == '}' and len(stack) > 0 and stack[-1] != '{': 
                return False
            if c == ']' and len(stack) > 0 and stack[-1] != '[':
                return False
            if c == ')' and len(stack) > 0 and stack[-1] != '(':
                return False 
            if c in closing:
                if len(stack) < 1:
                    return False
                else:
                    stack.pop()
          
        if len(stack) > 0: 
            return False
        else:
            return True 
            
                