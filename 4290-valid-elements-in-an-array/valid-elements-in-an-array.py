class Solution:
    def findValidElements(self, nums):
        n = len(nums)

        left_max = [0] * n
        right_max = [0] * n

        # build left max
        max_val = float('-inf')
        for i in range(n):
            left_max[i] = max_val
            max_val = max(max_val, nums[i])

        # build right max
        max_val = float('-inf')
        for i in range(n - 1, -1, -1):
            right_max[i] = max_val
            max_val = max(max_val, nums[i])

        # collect result
        res = []
        for i in range(n):
            if i == 0 or i == n - 1:
                res.append(nums[i])
            elif nums[i] > left_max[i] or nums[i] > right_max[i]:
                res.append(nums[i])

        return res