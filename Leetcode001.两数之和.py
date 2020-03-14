'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]'''

nums = [1,5,5]
target = 10
for i in range(len(nums)):
    for j in range(i + 1,len(nums)): #题目要求不可重复使用
        if nums[i] + nums[j] == target:
            print([i,j])
