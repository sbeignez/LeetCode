class Solution:
    def isNumber(self, s: str) -> bool:
        
        states = [
            {},
            # START
            # State (1) - Next: blank, sign, digit or dot
            {
                'sign': 2,
                'digit': 3,
                '.': 4
            },
            # State (2) - Found sign. Next: digit or dot
            {
                'digit':3,
                '.':4},
            # State (3) - digit consumer (loop until non-digit)
            {
                'digit':3,
                '.':5,
                'exp':6,
            },
            # State (4) - found dot (only a digit is valid)
            {
                'digit':5
            },
            # State (5) - after dot. Next: digits, exp
            {
                'digit':5,
                'exp':6,
            },
            
            # EXPONENT PART 
            # State (6) Found 'exp'. Next: sign (7) or digit (8)
            {
                'sign':7,
                'digit':8
            },
            # State (7) Found 'exp' and a 'sign' Next: only digit (8)
            {
                'digit':8
            },
            # State (8) Found 'exp' (and maybe a 'sign'). Next: digits or end
            {
                'digit':8,
            },
            
            ]
        
        currentState = 1
        
        for c in s:
            
            # Read tokens
            if c in '1234567890':
                c = 'digit'
            # elif c in ' \t\n':
            #    c = 'blank'
            elif c in '+-':
                c = 'sign'
            elif c in 'Ee':
                c = 'exp'
                
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            
            # Transition to next state
            currentState = states[currentState][c]
            
        # test for valid FINAL STATES
        if currentState not in [3,5,8]:
            return False
        
        return True
        
        