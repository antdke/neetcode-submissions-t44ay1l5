class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_store = {}

        for index, num in enumerate(nums):

            if target - num in index_store:
                return [index_store[target - num], index]

            index_store[num] = index

        return []