class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s[::-1].strip().split(" ")
        return len(a[0])


                