class Solution:
    def limitOccurrences(self, nums, k):
        write = 0

        for num in nums:
            if write < k or nums[write - k] != num:
                nums[write] = num
                write += 1

        return nums[:write]