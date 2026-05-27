class Solution:
    def mirrorDistance(self, n: int) -> int:
         reversed=int(str(n)[::-1])
         return abs(n-reversed)
