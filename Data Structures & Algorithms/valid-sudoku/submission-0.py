class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Sub problem 1: validate row
        for i in range(9):
            tmp = set()
            for j in range(9):
                x = board[i][j]
                if x in tmp:
                    return False
                elif x != ".":
                    tmp.add(x)
        
        #Sub problem 2: validate colums
        for i in range(9):
            tmp = set()
            for j in range(9):
                x = board[j][i]
                if x in tmp:
                    return False
                elif x != ".":
                    tmp.add(x)

        #Sub problem 3: validate sub-box
        start = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for init_r, init_c in start:
            tmp = set()
            for i in range(init_r, init_r + 3):
                for j in range(init_c, init_c + 3):
                    x = board[i][j]
                    if x in tmp:
                        return False
                    elif x != ".":
                        tmp.add(x)
        return True

        # Time: O(n^2), n = len(board)
        # Space: O(n)