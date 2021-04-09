class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        o = dict( zip (order , range(len(order))) ) 

        def isSorted(w1, w2):
              if not w1:
                  return True  
              if not w2:
                  return False               
              if o[w1[0]] > o[w2[0]]:
                  return False
              if o[w1[0]] < o[w2[0]]:
                  return True
              return isSorted(w1[1:],w2[1:])

        res , i = True, 0
        while res and i < len(words)-1:
            res = isSorted(words[i],words[i+1]) and res
            i += 1
              
        return res        