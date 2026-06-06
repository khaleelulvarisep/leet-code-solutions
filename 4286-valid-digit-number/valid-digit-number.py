class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        num=str(n)
        dig=str(x)
        if num[0]==dig:
            return False
        if dig in num:
            return True
        else:
            return False    
        