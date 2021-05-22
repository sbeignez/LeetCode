class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = pattern.upper()
        A = []
        for word in words:
            ok = True
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
                
            if ok: A.append(word)
        return A    