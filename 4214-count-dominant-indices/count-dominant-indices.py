class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            suum=0
            suum=sum(nums[i+1:])

            if suum:
                if suum/len(nums[i+1:])<nums[i]:

                    result+=1
        return result             
        



        