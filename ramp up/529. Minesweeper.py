class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(x, y):
            M = 0
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != "E":
                return
            for nx, ny in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                if  0 <= x+nx <len(board) and 0 <= y+ny < len(board[0]) and board[x+nx][y+ny] == "M":
                    M += 1
            if M == 0:
                board[x][y] = "B"
            else:
                board[x][y] = str(M)
                return
            for nx, ny in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                dfs(x+nx, y+ny)
            return
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            dfs(click[0], click[1])
        return board