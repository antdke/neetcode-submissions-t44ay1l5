class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # result array with fixed length with "1"s for easy multiply
        # forward pass with products going left to right
        # backward pass with products going right to left
        # use prefix/post fix to store intermediate values

        result = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result