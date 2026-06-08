class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for n in nums:
            if n%2==0 and nums.count(n)==1:
                return n
        return -1        
        