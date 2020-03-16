'''class Solution:
    def compressString(self, S: str) -> str:
        S += '.'
        lens = len(S)
        temp = ""
        count = 1
        for i in range(1,lens):
            if S[i] == S[i-1]:
                count += 1
            else:
                temp = temp + S[i-1] + str(count)
                count = 1
        if len(temp) < lens-1:
            return temp
        else:
            return S[:-1]'''

S = 'bb'
S += "."   #添加一个哨兵 用来检测原文最后一位字符
lens = len(S)
temp = ""   
count = 1
for i in range(1,lens):
    if S[i] == S[i-1]:  #相同的话计数+1  
        count += 1
    else:
        temp = temp + S[i-1] + str(count)  #不同了就将str储存到temp中 然后计数重新开始
        count = 1
        
if len(temp) < lens-1:
    print(temp)
else:
    print(S[:-1])

'''ori_len = len(S)     #不管有多少 统一计数 无脑写下来的
dic = {}
l = []
for i in S:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1
for string in S:
    if string not in l:
        l.append(string)
        l.append(dic[string])
print(dic)
res = ""
for item in l:
    res += str(item)
if len(res) < ori_len:
    print(res)
else:
    print(ori_len)'''