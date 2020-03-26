'''class Solution:
    def numRookCaptures(self,board: List[List[str]]) -> int:
        Rx, Ry = 0, 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    Rx, Ry = i, j
        countl = 0
        # 从左边开始
        for i in range(Ry):
            if board[Rx][i] == 'p':
                countl = 1
                continue
            if board[Rx][i] == 'B':
                countl = 0
        # 从右边开始
        countr = 0
        for i in range(Ry+1, len(board[Rx])):
            if board[Rx][i] == 'B':
                break
            elif board[Rx][i] == 'p':
                countr = 1
        # 从上边开始
        countu = 0
        for i in range(0,Rx):
            if board[i][Ry] == 'p':
                countu = 1
                continue
            if board[i][Ry] == 'B':
                countu = 0

        # 从下边开始
        countd = 0
        for i in range(Rx,len(board)):
            if board[i][Ry] == 'p':
                countd = 1
            if board[i][Ry] == 'B':
                break
        return countd + countu + countl + countr'''
        
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]


Rx, Ry = 0, 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'R':
            Rx, Ry = i, j
countl = 0
# 从左边开始
for i in range(Ry):
    if board[Rx][i] == 'p':
        countl = 1
        continue
    if board[Rx][i] == 'B':
        countl = 0
# 从右边开始
countr = 0
for i in range(Ry+1, len(board[Rx])):
    if board[Rx][i] == 'B':
        break
    elif board[Rx][i] == 'p':
        countr = 1
# 从上边开始
countu = 0
for i in range(0,Rx):
    if board[i][Ry] == 'p':
        countu = 1
        continue
    if board[i][Ry] == 'B':
        countu = 0

# 从下边开始
countd = 0
for i in range(Rx,len(board)):
    if board[i][Ry] == 'p':
        countd = 1
    if board[i][Ry] == 'B':
        break
print(countd + countu + countl + countr)

