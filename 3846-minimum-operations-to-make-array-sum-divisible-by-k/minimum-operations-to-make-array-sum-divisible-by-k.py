class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        suum=sum(nums)
        
        if suum%k==0:
            return 0
        else:
            r=suum%k
            return r



        