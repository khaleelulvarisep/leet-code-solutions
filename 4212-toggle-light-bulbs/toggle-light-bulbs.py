class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        result=[]
        for b in bulbs:
            if b not in result:
                if bulbs.count(b)%2!=0:
                    result.append(b)
        return sorted(result)    


        