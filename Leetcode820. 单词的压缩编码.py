'''class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))          #按单词长度排序
        ans = ''                                    #目标字符串
        for i in range(len(words)-1, -1, -1):       #按单词长度从长到短遍历（逆序循环）
            tmp = ans.find(words[i])                #单词是否在目标字符串中，若存在，返回索引
            if tmp == -1:                           #单词不在目标字符串中，添加进去
                ans += words[i] + '#'
            else:                                   #单词在目标字符串中，判断能否完全读取
                x = ans[tmp:].index('#')            #获取单词后第一个“#”索引
                if ans[tmp:tmp+x] != words[i]:      #判断是否能够完全读取，若不能，添加单词
                    ans += words[i] + '#'
        return len(ans)                             #返回目标字符串长度'''


words = ["time", "me", "bell"]  
words.sort(key = lambda x: len(x))          #按单词长度排序
ans = ''                                    #目标字符串
for i in range(len(words)-1, -1, -1):       #按单词长度从长到短遍历（逆序循环）
    tmp = ans.find(words[i])                #单词是否在目标字符串中，若存在，返回索引
    if tmp == -1:                           #单词不在目标字符串中，添加进去
        ans += words[i] + '#'
    else:                                   #单词在目标字符串中，判断能否完全读取
        x = ans[tmp:].index('#')            #获取单词后第一个“#”索引
        if ans[tmp:tmp+x] != words[i]:      #判断是否能够完全读取，若不能，添加单词
            ans += words[i] + '#'
print(len(ans))                          #返回目标字符串长度