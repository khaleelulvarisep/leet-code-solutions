class Solution:
    
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        result=[]
        y=[]
        freq={}
        for n in nums:
            if n not in freq:
                freq[n]=nums.count(n)
        x=min(nums)
        for n in nums:
            if x<n and freq[x]!=freq[n]:
                y.append(n)

        result.append(x)
        if y:
            result.append(min(y))
        else:
            return [-1,-1]    
        print(y)
        return result        



           
                         
        
              

        