class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if 1 not in nums or 2 not in nums:
            return -1
        pairs=[]    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i] ==1:
                    if nums[j]==2:
                        pairs.append(abs(i-j))
                elif nums[i]==2:
                    if nums[j]==1:
                        pairs.append(abs(i-j))
        return min(pairs)                


        