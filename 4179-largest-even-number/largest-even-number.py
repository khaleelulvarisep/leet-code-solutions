class Solution:
    def largestEven(self, s: str) -> str:
       
        if s[len(s)-1]=='2':
            return s
        if '2' not in s:
            return ''    
           
        for i in range(len(s)):
            if s[len(s)-1]=='2':
                return s
            elif s[len(s)-1-i]=='2':
                return s[:len(s)-1-i+1]




        