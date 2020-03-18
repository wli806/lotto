'''class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool::
        x1 = max(rec1[0],rec2[0])
        x2 = min(rec1[2],rec2[2])

        y1 = max(rec1[1],rec2[1])
        y2 = min(rec1[3],rec2[3])
        if x1 < x2 and y1 < y2:
            return True
        else:
            return False'''

rec1 = [0,0,2,2],
rec2 = [1,1,3,3]

#找两个图从座标上看的共同域

x1 = max(rec1[0],rec2[0])  #左上角的最大值若是比右下角的最小值大 那么就不构成
x2 = min(rec1[2],rec2[2])  #同理

y1 = max(rec1[1],rec2[1])
y2 = min(rec1[3],rec2[3])
if x1 < x2 and y1 < y2:
    print(True)
else:
    print(False)
