class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result=[]
        m=min(nums)
        l=max(nums)
        j=m

        while j<l:
            if j not in nums:
                result.append(j)
            j+=1  
        return result        


        

        