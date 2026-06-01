class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=nums[i]
            total=0
            while n>0:
                digit=n%10
                total+=digit
                n//=10
            nums[i]=total

        return min(nums)        



        