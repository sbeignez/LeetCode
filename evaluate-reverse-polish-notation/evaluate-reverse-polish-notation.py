import math
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: math.trunc(a / b),
            }
        
        S = []

        for token in tokens:
            if token in op:
                b = S.pop()
                a = S.pop()
                f = op[token]
                S.append(f(a,b))
            else:
                S.append(int(token))

        return S[0]
        