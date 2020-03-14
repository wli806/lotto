'''class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) < 1:
            return 0
        dp = [1] * len(nums)
        res = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            if res < dp[i]:
                res = dp[i]
        return res'''
nums = [4,1,6,2,3,8]
if len(nums) < 1:
    print(0)
dp = [1] * len(nums)  #为每个数字创建位置 来储存上升子序列长度
res = 1  #初始长度  所以即使是最短的一个数也是count 1
for i in range(1,len(nums)):  #这里用1是为了当i=1是有index[0]来比较
    for j in range(i):  #用j来表示i之前的数字
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j]+1)  #dp[i]这步更新当前i对应的最大子序列 下一次运算j就是这次的i 更新了最长值 所以一旦nums[i]>nums[j]就看现在和之前j+1哪个更长 储存长度
    if res < dp[i]:  #取最大值
        res = dp[i]
print(res)




