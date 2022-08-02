class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        que = deque()
        visited = [[False] * n for _ in range(m)]
        answer = 0
        for i in range(m):
            for j in range(n):
                # run bfs
                area = 0
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    que.append([i, j])

                    while que:
                        area += 1
                        x, y = que.popleft()
                        if x - 1 >= 0 and not visited[x - 1][y] and grid[x - 1][y] == 1:
                            visited[x - 1][y] = True
                            que.append([x - 1, y])
                        if y + 1 < n and not visited[x][y + 1] and grid[x][y + 1] == 1:
                            visited[x][y + 1] = True
                            que.append([x, y + 1])
                        if x + 1 < m and not visited[x + 1][y] and grid[x + 1][y] == 1:
                            visited[x + 1][y] = True
                            que.append([x + 1, y])
                        if y - 1 >= 0 and not visited[x][y - 1] and grid[x][y - 1] == 1:
                            visited[x][y - 1] = True
                            que.append([x, y - 1])
                    answer = max(answer, area)
        return answer
