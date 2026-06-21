class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        result=0
        for n in nums:
            if nums.count(n)%k==0:
                result+=n
        return result        