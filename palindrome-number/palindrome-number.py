class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        l = len(n)
        
        out = True
        for i in range(0,int(round(l/2,0))):
            # print(f"i={i} {n[i]} vs {n[l-i-1]}")
            out = out and (n[i] == n[l-i-1])
        return out
        