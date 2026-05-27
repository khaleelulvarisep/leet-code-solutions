class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        result=[]
        for i in range(len(nums)):
            result.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            result.append(nums[i])

        return result    
