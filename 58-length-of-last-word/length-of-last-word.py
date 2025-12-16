class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = []
        a = s[::-1]
        z = a.strip()
        c = z.split(" ")
        return len(c[0])


                