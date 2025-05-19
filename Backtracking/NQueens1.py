class Solution:
    def solveNQueens(self,n:int)->List[List[str]]:
        def is_valid(row,col):
            return col not in cols and (row+col) not in diag1 and (row-col) not in diag2

        def backtrack(row,board):
            if row==n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if is_valid(row,col):
                    cols.add(col)
                    diag1.add(row+col)
                    diag2.add(row-col)
                    board[row][col]='Q'
                    backtrack(row+1,board)
                    board[row][col]='.'
                    cols.remove(col)
                    diag1.remove(row+col)
                    diag2.remove(row-col)

        result=[]
        cols=set()
        diag1=set()
        diag2=set()
        board=[['.']*n for _ in range(n)]
        backtrack(0,board)
        return result
