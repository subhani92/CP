class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        paranthesis = { "(":")", "{":"}", "[":"]" }

        if not s:
            return True
        
        for char in s:
            #(
            if char in paranthesis.keys():
                stack.append(char)
            else:
                if stack: # if stack is not empty 
                    if paranthesis[stack[-1]] == char:
                        stack.pop()
                    else: #"[}"
                        return False 
                else: #"s = ]" 
                    return False 
                    
        return len(stack) == 0 

