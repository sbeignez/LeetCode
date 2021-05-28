# https://leetcode.com/problems/n-queens/
# 51. N-Queens
# May Challenge: May 22


from typing import List
import copy

print("start")

tests = [
    [1, [["Q"]] ], 
    [2, []], 
    [3, []],
    [4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]],
    # [9, []],
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [ '.' * n for _ in range(n)]

        def isSolution(board, last_count) -> bool:

            count = 0
            crow = [0] * n
            ccol = [0] * n
            cdown = [0] * (2*n)
            cup = [0] * (2*n)

            for r in range(n):
                for c in range(n):
                    if board[r][c] == "Q":
                        if crow[r] == 1: return False
                        else: crow[r] += 1

                        if ccol[c] == 1: return False
                        else: ccol[c] += 1

                        if cdown[r+c] == 1: return False
                        else: cdown[r+c] += 1

                        if cup[r-c+n] == 1: return False
                        else: cup[r-c+n] += 1

                        if count == n: return False
                        else:
                            count += 1

                        if count == last_count:
                            if count == n: return True
                            else: return None
            
            if count == n: return True
            else: return None



        def expand(board, row, col, count) -> List[List[str]]:

            boards = []
            count += 1
            
            for r in range(row+1,n):
                for c in range(n):
                    new_board = board.copy()
                    new_board[r] = new_board[r][:c] + "Q" + new_board[r][c+1:]
                    boards.append((new_board, r, c, count))

            return boards


        def backtrack(board, max_row, max_col, count = 0):
            # print(board)
            check = isSolution(board, count)
            if check == False:
                return False
            if check == True:
                solutions.append(board)
                return True
            
            for b, r, c, count in expand(board, max_row, max_col, count):
                backtrack(b, r, c, count)

        backtrack(board, -1, -1)

        return solutions
            

      
testing(Solution().solveNQueens, tests)





'''
q_per_row =  all( sum( 1 for c in range(n) if board[r][c] == QUEEN ) <= 1 for r in range(n) )
if not q_per_row: return False

q_per_col =  all( sum( 1 for r in range(n) if board[r][c] == QUEEN ) <= 1 for c in range(n) )
if not q_per_col: return False

q_per_diagonal_down =  all( sum( 1 for r in range(n) for c in range(n) if (r+c == s) and (board[r][c] == QUEEN) ) <= 1  for s in range(2*n))
if not q_per_diagonal_down: return False

q_per_diagonal_up =  all( sum( 1 for r in range(n) for c in range(n) if (r-c == s) and (board[r][c] == QUEEN) ) <= 1  for s in range(-n+1,n))
if not q_per_diagonal_up: return False


n_q = sum( 1 for r in range(n) for c in range(n) if board[r][c] == QUEEN ) == n
if n_q:
    return True
else:
    return None
'''