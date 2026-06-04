class Solution:
    def limitOccurrences(self, nums, k):
        write = 0

        for num in nums:
            # allow first k elements always
            if write < k:
                nums[write] = num
                write += 1

            # after k elements, check last k element condition
            elif nums[write - k] != num:
                nums[write] = num
                write += 1

        return nums[:write]