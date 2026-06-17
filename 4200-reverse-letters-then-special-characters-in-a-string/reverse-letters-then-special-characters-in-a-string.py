class Solution:
    def reverseByType(self, s: str) -> str:

        spl="!@#$%^&*()" 
        rvsd=''
        rspl=''
        rltr=''
        result=''
        for i in range(len(s)-1,-1,-1):
            rvsd+=s[i] 
        for l in rvsd:
            if l in spl:
                rspl+=l
            else:
                rltr+=l
        i=0
        j=0
        for l in s:
            if l in spl:
                result+=rspl[i]
                i+=1
            else:
                result+=rltr[j] 
                j+=1   
        return result







               
                    

        
        

        