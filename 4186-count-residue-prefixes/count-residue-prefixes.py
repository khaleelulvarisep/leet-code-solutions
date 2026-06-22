class Solution:
    def residuePrefixes(self, s: str) -> int:
        freq = [0] * 26
        distinct = 0
        count = 0

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')

            if freq[idx] == 0:
                distinct += 1
            freq[idx] += 1

            prefix_len = i + 1
            if distinct == prefix_len % 3:
                count += 1

        return count     

        