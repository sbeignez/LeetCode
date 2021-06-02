class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        d = 1
        i = len(digits)-1
        
        while d == 1:
            n = digits[i]
            d , u = (n+1) // 10, (n+1) % 10
            digits[i] = u
            
            i -=1
            if i == -1 and d:
                digits = [1] + digits
                break
        
        return digits
            
        