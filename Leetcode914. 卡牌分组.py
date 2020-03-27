'''class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        l = len(deck)

        if l < 2:
            return False

        d = {}
        for i in deck:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] = d[i] + 1

        m = min(d.values())
        if m < 2:
            return False
        import math
        k = math.gcd(l, m)
        if k == 1:
            return False
        tmp = k
        for v in d.values():
            tmp = math.gcd(v, tmp)
        if tmp < 2:
            return False
        return True

'''

deck = [1,2,3,4,4,3,2,1]
l = len(deck)

if l < 2:
    print(False)

d = {}
for i in deck:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] = d[i] + 1

m = min(d.values())
if m < 2:
    print(False)
import math
k = math.gcd(l, m)
if k == 1:
    print(False)
tmp = k
for v in d.values():
    tmp = math.gcd(v, tmp)
if tmp < 2:
    print(False)
print(True)