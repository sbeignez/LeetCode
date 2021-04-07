class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
      # L = len(s) // 2
      # delta = sum( (s[i] in vowels) - (s[L+i] in vowels) for i in range(L)) == 0
      # return delta 
        
      L = len(s) // 2
      i, c1, c2 = 0, 0, 0
      
      while i < L and abs(c1 - c2) <= L - i :
        if s[i] in vowels:
          c1 += 1
        if s[i+L] in vowels:
          c2 += 1  
        i += 1
         

      return c1 == c2