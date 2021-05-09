import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        if len(target) == 1:
            if not target[0] == 1:
                return False
            else:
                return True
        
        X = [ -x for x in target]
        heapq.heapify(X)
        T = sum(target)
        print(X)

        while True:
            x = - heapq.heappop(X)
            R = T - x
            if x == 1 or R == 1: return True
            prev = x % R
            if R >= x or not prev: return False
            T = T - (x - prev)
            heapq.heappush(X, -prev)