# Name: 6. Zigzag Conversion
# Link: https://leetcode.com/problems/zigzag-conversion/


from typing import List

tests = [
    ["PAYPALISHIRING", 3 , "PAHNAPLSIIGYIR"],
    ["PAYPALISHIRING", 4 , "PINALSIGYAHRPI"],
    ["A", 1 , "A"],
    ["A", 2 , "A"],

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
import itertools

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ""
        if numRows == 1: return s
        for row in range(numRows):
            print(len(s) , numRows, len(s) // (2 * numRows - 2) + 1)
            for i in range( len(s) // (2 * numRows - 2) + 1):
                a = (row + (2 * numRows - 2)* i)
                A = s[a] if a < len(s) else ""

                b = (2 * numRows - 2) * (i+1) - row              
                B = s[b] if (row not in [0, numRows -1]) and (b < len(s)) else ""
                print(row, A,B)
                ans = ans + A + B
        return ans

      

             

      
testing(Solution().convert, tests)



