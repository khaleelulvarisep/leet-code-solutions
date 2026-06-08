class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        cut=0
        vwl='aeiou'
        for i in range(len(s)-1,-1,-1):
            if s[i] in vwl:
                cut=i
                if cut==0:
                    return ''
            else:
                break
        if cut==0:
            return s
        else:
            return s[:cut]    


            
