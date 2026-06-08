class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        elig=[]    
        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                elig.append(capacity[i])
        if elig:
            return capacity.index(min(elig)) 
        else:
            return -1           

                

           
               


