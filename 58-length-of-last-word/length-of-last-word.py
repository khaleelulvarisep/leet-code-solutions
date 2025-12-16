class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s[::-1]
        z = a.strip().split(" ")
        # c = z.split(" ")
        return len(z[0])


                