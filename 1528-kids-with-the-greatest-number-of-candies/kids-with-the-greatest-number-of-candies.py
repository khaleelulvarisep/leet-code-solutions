class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]

        for cand in candies:
            if cand+extraCandies>=max(candies):
                result.append(True)
            else:
                result.append(False)    

        return result        

        