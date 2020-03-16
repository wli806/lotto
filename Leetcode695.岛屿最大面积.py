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
    if i < 0 or i >= m or j < 0 or j >= n:  # i,j>= 0是为了bot l, i<m j<n是为了top r
        return 0
    if grid[i][j] == 0:  #=0说明不是小岛 对于此[i][j]返回0
        return 0
    else:
        grid[i][j] = 0  #return有+1 直接让他变0 因为只要连续就算一起 所以变0不影响找下一组小岛 所以=0不再看他  后续dfs同理      
        top = dfs(i - 1, j)
        bottom = dfs(i + 1, j)
        left = dfs(i, j - 1)
        right = dfs(i, j + 1)  #这四个操作 一旦发现不为0 则我们要用新的t,b,l,r进行dfs运算 知道返回值 不断返回 recursive来获取最大值 一旦完成这一部分的小岛值 接下来就可以去看下一块小岛   因为查过的小岛都为0  不必担心重复count事实上也不可能出现重复count
        return 1 + sum([top, bottom, left, right])
    
for i in range(m):  #行序号
    for j in range(n):  #列序号
        ans = max(ans, dfs(i, j))  #[i][j]可以定位到固定数字 DFS   max选出最大值 返回即为答案
print(ans)