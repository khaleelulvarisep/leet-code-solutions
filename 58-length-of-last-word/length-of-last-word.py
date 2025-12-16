class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s[::-1]
        z = a.strip()
        c = z.split(" ")
        return len(c[0])


                