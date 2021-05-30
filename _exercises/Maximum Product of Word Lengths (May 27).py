# 
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3757/
# ??. Maximum Product of Word Lengths
# May Challenge: May 27


from typing import List

print("start")

tests = [
    [["abcw","baz","foo","bar","xtfn","abcdef"], 16 ],

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

import itertools
class Solution:
    def maxProduct(self, words: List[str]) -> int:

        print(words)

        # create a list of set of words by length
        W = {}
        for word in words:
            L = len(word)
            word = set(word) # ''.join(sorted(set(word)))
            W[L] = W.get(L,[]) + [word]
        print(W)

        keys = list(W.keys())
        print(keys)

        # create the combination of length to test in desc order
        N = [ (item[0]*item[1],item[0],item[1]) for item in itertools.combinations_with_replacement( keys, 2)]
        N.sort(key = lambda x : x[0], reverse=True)
        print(N)

        # loop the sets
        for n in N:
            for w1 in W[n[1]]:
                for w2 in W[n[2]]:
                    print(w1,w2, w1 & w2)
                    if not w1 & w2:
                        return n[0]
        
        return 0

      

            

      
testing(Solution().maxProduct, tests)



