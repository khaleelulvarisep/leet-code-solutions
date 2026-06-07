class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        result=[]
        
        for i in range(len(nums)):
            stbl=0
            if i==0:
                stbl=nums[0]-min(nums)
                if stbl<=k:
                    result.append(i)
                continue
            stbl=max(nums[:i])-min(nums[i:])
            if stbl<=k:
                result.append(i)
        if result:
            return min(result)
        else:
            return -1                



             


        