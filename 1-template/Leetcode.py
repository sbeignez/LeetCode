from typing import List

print("start")

tests = [
    [["abc","deq","mee","aqq","dkd","ccc"], "abb", ["mee","aqq"]], 
    [["a","b","c"], "a", ["a","b","c"]],
]

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


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = pattern.upper()
        A = []
        print("P", pattern)
        for word in words:
            ok = True
            print("W", word)
            D = {}
            
            for index, letter in enumerate(pattern):
                w = word[index]
                if w not in D.keys():
                    if letter not in D.values():
                        D[w] = letter
                    else:
                        ok = False
                else:
                    if D[w] is not letter:
                        ok = False
                print(D)
                
            if ok: A.append(word)
        return A


    def findAndReplacePattern2(self, words: List[str], pattern: str) -> List[str]:
        pattern = pattern.upper()
        A = []
        print("P", pattern)
        for word in words:
            ok = True
            print("W", word)
            D = {}
            
            for index, letter in enumerate(pattern):
                w = word[index]
                if w not in D.keys():
                    if letter not in D.values():
                        D[w] = letter
                    else:
                        ok = False
                else:
                    if D[w] is not letter:
                        ok = False
                print(D)
                
            if ok: A.append(word)
        return A


testing(Solution().findAndReplacePattern2, tests)