class Solution:
    
    def vowelConsonantScore(self, s: str) -> int:
        vowels='aeiou'
        aplpha='abcdefghijklmnopqrstuvwxyz'
        v=0
        c=0
        for m in s:
            if m in vowels:
                v+=1
            elif m in aplpha:
                c+=1    
           
        
        if c>0:
            score=v//c     
        else:
            score=0
        return score        

        print(v)


