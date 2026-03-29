class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # left -> 0
        # right -> len(numbers) - 1
        # while left < right
        # sum = numbers[left] + numbers[right]
        # if sum < target
        # left += 1
        # continue
        # if sum > target
        # right -= 1
        # continue
        # return [left + 1, right + 1]

        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
                continue
            if sum > target:
                right -= 1
                continue
            return [left + 1, right + 1]