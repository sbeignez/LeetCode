# Name: 
# Link: https://leetcode.com/explore/challenge/


from typing import List

tests = [
    ["abcabcbb", 3],
    ["bbbbb", 1],
    ["pwwkew",3]

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
# import itertools

      
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        m = 0

        for c in s:
            if c not in sub:
                sub = sub + c
                m = max(m, len(sub))
            else:
                sub = sub[ sub.find(c)+1 : ] + c

        return m
        
        
            

      
testing(Solution().lengthOfLongestSubstring, tests)



