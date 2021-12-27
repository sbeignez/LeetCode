# Name: 
# Link: https://leetcode.com/explore/challenge/


from typing import List

tests = [
    [["input"], "ouput" ],

]
print("TESTS", tests)

def testing(f,tests):
    print("  ======================")
    success = True
    for i, test in enumerate(tests):
        args = test[:-1]
        expected = test[-1]

        print(f"  Test {i}: {args} --> {expected}.")
        res = f(*args)
        success = success and res==expected
        print(f"  {res==expected}\t OUT:{res}\t EXP:{expected}\t IN:{args}\t ")
        print("  -----------------------")
    print(f"  Success: {success}")
    print("  ======================")


# =============================
import itertools

class Solution:
    def xxx(self, words: List[str]) -> int:
        A = None
       
        
        return A

      

            

      
testing(Solution().xxx, tests)



