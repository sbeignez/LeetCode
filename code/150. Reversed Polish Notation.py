# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3755/
# 150. Evaluate Reverse Polish Notation
# May Challenge: May 24


from typing import List

print("start")

tests = [
    [["2","1","+"], 3 ],
    [["2","1","+","3","*"], 9 ],
    [["4","13","5","/","+"], 6],
    [["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22],
]
print(tests)

def testing(f,tests):
    success = True
    for i, test in enumerate(tests):
        args = test[:-1]
        expected = test[-1]
        print("-----------------------")
        print(f"Test {i}: {args} --> {expected}.")

        res = f(*args)

        success = success and res==expected
        print(f"{res==expected}\t OUT:{res}\t EXP:{expected}\t IN:{args}\t ")
    print("======================")
    print(f"Success: {success}")



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

            

      
testing(Solution().evalRPN, tests)



