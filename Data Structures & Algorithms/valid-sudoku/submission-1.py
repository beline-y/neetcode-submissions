class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line = [0]*9
        columns = [0]*9
        box = [0]*9
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c])-1
                if (1<<val) & line[r]:
                    return False
                if (1<<val) & columns[c]:
                    return False
                if (1<<val) & box[(r // 3) * 3 + (c // 3)]:
                    return False
                
                line[r] |= (1 << val)
                columns[c] |= (1 << val)
                box[(r // 3) * 3 + (c // 3)] |= (1 << val)
        return True
                


        