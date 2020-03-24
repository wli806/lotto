'''class Solution:
    def massage(self, nums: List[int]) -> int:
        nmax1 = nmax2 = 0
        i = 0
        while i < len(nums):
            nmax1 , nmax2 = max(nmax1,nmax2+nums[i]) , nmax1
            i +=1
        return nmax1'''

nums = [1,2,3,1]
nmax1 = nmax2 = 0
i = 0
while i < len(nums):
    nmax1 , nmax2 = max(nmax1,nmax2+nums[i]) , nmax1
    i +=1
return nmax1