'''class Solution:
    def majorityElement(self, nums):  #没动脑直接顺着做 想到了字典
        most = round(len(nums) / 2 + 0.01)  #找出题目中的多数元素
        numdic = {}
        result = []
        for item in nums:
            if item not in numdic.keys(): #list中的值 没有则建立
                numdic[item] = 1
            else: #有则数量加1
                numdic[item] += 1
        for k,v in numdic.items(): #根据value找key
            if v >= most:
                result.append(k)
        for num in result:
            return num  #返回key  相当于众数'''

nums = [1,1,2,2,2,2,2]
most = round(len(nums) / 2 + 0.01)  #找出题目中的多数元素
numdic = {}
result = []
for item in nums:
    if item not in numdic.keys(): #list中的值 没有则建立
        numdic[item] = 1
    else: #有则数量加1
        numdic[item] += 1
for k,v in numdic.items(): #根据value找key
    if v >= most:
        result.append(k)
for num in result:
    print(num)  #返回key  相当于众数
