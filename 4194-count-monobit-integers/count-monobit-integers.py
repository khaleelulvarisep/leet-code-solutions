class Solution:
    def countMonobit(self, n: int) -> int:
        m=1

        while 2**m-1<=n:
            m+=1

        return m  
        