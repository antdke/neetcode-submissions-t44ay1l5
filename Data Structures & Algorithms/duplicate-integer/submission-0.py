class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # set to store unique values

        # iterate over nums

        # if element in set -> return True

        # store each element

        # return False

        unique_values = set()

        for num in nums:
            print(num)

            # True -> contains dupe
            if num in unique_values:
                return True
            
            unique_values.add(num)

        # False -> does NOT contain dupe
        return False