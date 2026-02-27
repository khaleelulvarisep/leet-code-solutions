class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        t=True
        f=False
        for cand in candies:
            if cand+extraCandies>=max(candies):
                result.append(t)
            else:
                result.append(f)    

        return result        

        