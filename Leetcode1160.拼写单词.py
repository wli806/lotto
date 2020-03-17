'''class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int::
        res = 0
        for word in words:
            lens = len(word)
            temp = 0
            for i in word:
                if word.count(i) <= chars.count(i):
                    temp += 1
                else:
                    break
            if temp == lens:
                res += len(word)
        return res'''
words = ["cat","bt","hat","tree"]
chars = "atach"
res = 0
for word in words:
    lens = len(word)  #下面的for loop中与temp储存值进行比较  相等说明所有字符都在chars中数量也符合
    temp = 0
    for i in word:
        if word.count(i) <= chars.count(i):  #.count() 函数的使用  求该字符的和
            temp += 1  #+1表示该数位满足
        else:
            break #提高速度 不符合就出这个for loop 进行下一个word
    if temp == lens:
        res += len(word)  #符合就增加字符长度
print(res)