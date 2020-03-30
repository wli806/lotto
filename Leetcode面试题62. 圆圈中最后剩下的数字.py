'''class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (m + x) % i
        return x'''
        
n = 5
m = 3
x = 0
for i in range(2, n + 1):
    x = (m + x) % i
print(x)