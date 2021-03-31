class Solution:
    def isValid(self, s: str) -> bool:
        
        p = { "(": ")", "{": "}", "[": "]" }
        stack = list()
        
        for i in range(0,len(s)):
            if s[i] in p:
                stack.append(s[i])
            else:
                if len(stack) and ( p[stack[-1]] == s[i] ):
                    stack.pop()
                else:
                    return False
        return not len(stack)
                