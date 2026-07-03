from typing import List

class Solution:
    def countOppositeParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        even = 0
        odd = 0

        for i in range(n - 1, -1, -1):
            if nums[i] % 2 == 0:
                answer[i] = odd
                even += 1
            else:
                answer[i] = even
                odd += 1

        return answer