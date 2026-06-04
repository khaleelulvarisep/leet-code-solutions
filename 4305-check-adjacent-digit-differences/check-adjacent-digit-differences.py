class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s)-1):
            j=i+1
            f=int(s[i])
            m=int(s[j])

            if(abs(f-m))>2:
                return False
                                                           
        return True    
            



        

