'''class Solution:
    def longestPalindrome(self, s: str) -> int:
        #统计字符词频
        s_cnt = collections.Counter(s)
        center = 0
        res = 0
        for char in s_cnt:
            #判断各个字符的词频奇偶
            if s_cnt[char] % 2:
                center = 1 #若出现奇数频次，center置为1
                res += s_cnt[char] - 1
            else:
                res += s_cnt[char]
        return res + center'''
import collections
s = "abccccdd"
s_cnt = collections.Counter(s)
center = 0

res = 0
for char in s_cnt:
    #判断各个字符的词频奇偶
    if s_cnt[char] % 2:
        center = 1 #若出现奇数频次，center置为1
        res += s_cnt[char] - 1
    else:
        res += s_cnt[char]
ans = res + center
print(ans)