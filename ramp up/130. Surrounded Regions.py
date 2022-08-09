class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(sr,sc):
            stk=[(sr,sc)]
            visited=set()
            goal=board[sr][sc]
            while stk:
                temp=stk.pop()
                visited.add(temp)
                # board[temp[0]][temp[1]]=color
                ways=[(temp[0],temp[1]+1),(temp[0]+1,temp[1]),(temp[0],temp[1]-1),(temp[0]-1,temp[1])]
                for pair in ways:
                    if pair[0] in range(len(board)) and pair[1] in range(len(board[0])):
                        if board[pair[0]][pair[1]]==goal and pair not in visited:
                            stk.append(pair)
            for i in visited:
                if i[0] not in range(1,len(board)-1) or i[1] not in range(1,len(board[0])-1):
                    return
            for i in visited:
                board[i[0]][i[1]]="X"
            return 
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n]=="O":
                    b=check(m,n)
            