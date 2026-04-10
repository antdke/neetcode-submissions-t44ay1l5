class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create map
        # enumerate nums list
        # for each element
            # check if target - element exists as key
                # if so return [map[target - element], current_index]
            # store target - element as key, index as value
        
        two_sum_map = collections.defaultdict(int)

        for index, num in enumerate(nums):
         
            if target - num in two_sum_map:
                return [two_sum_map[target - num], index]

            two_sum_map[num] = index

        


