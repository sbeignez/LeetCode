class Solution:
    
    romanDict = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    
    def romanToInt(self, s: str) -> int:
        if len(s) >= 2:
            sign = -1 if (self.romanDict.get(s[0]) < self.romanDict.get(s[1])) else 1
            return self.romanToInt(s[1:]) + self.romanDict.get(s[0]) * sign
        if len(s) == 1:
            return self.romanDict.get(s[0])
