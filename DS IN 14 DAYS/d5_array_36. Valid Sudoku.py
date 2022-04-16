class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            
        rows = [ {} for _ in range(9)]
        cols = [ {} for _ in range(9)]
        sections = [[ {} for __ in range(3) ] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # for rows
                if val in rows[r]:
                    return False
                rows[r][val] = True
                
                # for cols
                if val in cols[c]:
                    return False
                cols[c][val] = True
                
                # for 9 sections
                if val in sections[r//3][c//3]:
                    return False
                sections[r//3][c//3][val] = True
        return True