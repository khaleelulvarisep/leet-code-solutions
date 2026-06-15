class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:

        sort=sorted(nums)
        
        mini=sum(sort[:k])
        
        large=sum(sort[len(nums)-k:])
       
        return abs(mini-large)

        
            
            

        