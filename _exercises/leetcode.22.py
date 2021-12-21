## https://leetcode.com/problems/generate-parentheses/

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

# Brute force

from typing import List
import itertools

class Solution:

    char = ['(', ')']

    def generateParenthesis(self, n: int) -> List[str]:
        return [l for l in self.generateAll(n) if self.isValid(l)]

    def generateAll(self,n):
        L1 = {"".join(c) for c in itertools.permutations(self.char*n) }
        # L1 = ['']
        # for _ in range(n*2):
        #     L2 = []
        #     for item in L1:
        #         L2 = L2 + [item + c for c in self.char]
        #     L1 = L2
        return L1

    def isValid(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif count > 0:
                count -= 1
            else:
                return False
        return (count == 0)



# print(["".join(c) for c in itertools.permutations('abc') ])

s = Solution().generateAll(2)
print(list(s))

s = Solution().generateParenthesis(2)
print(s)







# n = 3

# S = {''}
# for i in range(n):
#     X = set()
#     for s in S.copy():
#         X.add('()' + s) 
#         X.add('(' + s + ')') 
#         X.add(s + '()') 
#     S = X.copy()

# list(X).sort()
# print(X)


# S = ['(', ')'] * n
# SS = [ "".join(x) for x in itertools.permutations(S,n*2)] 
# print(S)
# print(SS)


