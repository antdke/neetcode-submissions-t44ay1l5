class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:

            if num - 1 in num_set:
                continue

            curr_length = 1

            while num + curr_length in num_set:
                curr_length += 1

            max_length = max(max_length, curr_length)

        return max_length