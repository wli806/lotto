'''class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        ans = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n: return 0
            if grid[i][j] == 0: return 0
            grid[i][j] = 0
            top = dfs(i + 1, j)
            bottom = dfs(i - 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            return 1 + sum([top, bottom, left, right])
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
'''

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

m = len(grid)
if m == 0:
    print(0)
n = len(grid[0])
ans = 0
def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0
    if grid[i][j] == 0:
        return 0
    else:
        grid[i][j] = 0
        top = dfs(i + 1, j)
        bottom = dfs(i - 1, j)
        left = dfs(i, j - 1)
        right = dfs(i, j + 1)
        return 1 + sum([top, bottom, left, right])
for i in range(m):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)

