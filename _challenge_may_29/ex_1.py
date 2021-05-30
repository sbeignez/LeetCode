# Biweekly Contest 53
# Name: 
# Link: https://leetcode.com/contest/biweekly-contest-53

# from typing import List

tests = [
    [ "xyzzaz", 1 ],
    [ "aababcabc", 4 ],
    [ "aa", 0 ],
    [ "aabcaaa", 2 ],

]
print("TESTS", tests)

def testing(f,tests):
    print("======================")
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

# =============================
# import itertools

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        A = 0
        L = 3

        if len(s) < L: return A
        for i in range(len(s)-L+1):
            print(s[i:i+3])
            if len(set(s[i:i+3])) == L:
                A +=1

        return A

      

            
      
testing(Solution().countGoodSubstrings, tests)



