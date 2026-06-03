class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
       count=nums.count(0)
       sub=nums[len(nums)-count:]
       return count-sub.count(0)

        
           

        