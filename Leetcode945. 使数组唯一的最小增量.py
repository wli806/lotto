'''class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = 0
        temp = 0
        ans = ope(A)
        return ans

    def ope(A):
        count = 0
        for i in range(len(A),-1,-1):
            if count(A[i]) > 0:
                A[i] = A[i]+1
                count += 1
                ope(A)
            else:
                return count'''

'''class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # 贪心算法
        A.sort()
        count = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                count += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        return count'''

A = [3,2,1,2,1,7]
A.sort()
count = 0
for i in range(1, len(A)):
    if A[i] <= A[i - 1]:
        count += A[i - 1] - A[i] + 1
        A[i] = A[i - 1] + 1
print(count)


