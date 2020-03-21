'''class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x+y <z:
            return False
        else:
            return z % math.gcd(x,y) == 0'''
            
#贝祖定理 ax+by=z 有解当且仅当 z 是x, y的最大公约数的倍数 因此我们只需要找到 x, y 的最大公约数并判断 z 是否是它的倍数即可。
import math

x = 3
y = 5
z = 4
 
if z == 0:
    print(True)
if x + y < z:
    print(False)
else:
    print(z % math.gcd(x,y) == 0)