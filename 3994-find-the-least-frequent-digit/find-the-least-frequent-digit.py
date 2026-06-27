class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = {}

        for digit in str(n):
            d = int(digit)
            freq[d] = freq.get(d, 0) + 1

        min_freq = min(freq.values())

        for digit in sorted(freq):
            if freq[digit] == min_freq:
                return digit


       
        