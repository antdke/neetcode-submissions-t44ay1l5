class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        nums.sort()

        for index in range(len(nums)):

            if nums[index] > 0:
                break

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # get twoSum pairs
            pairs = self.twoSum(nums[index], index + 1, nums)

            # add all pairs to triplets
            for pair in pairs:
                triplets.append(pair + [nums[index]])
            
        return triplets

    # two sum
    def twoSum(self, current_element, next_index, nums):

        target = current_element * -1
        pairs = []
        left = next_index
        right = len(nums) - 1

        while left < right:
            print(left)
            print(right)
            two_sum = nums[left] + nums[right]

            if two_sum == target:
                # add pair to pairs
                pairs.append([nums[left], nums[right]])
                # increment left by 1
                left += 1
                # while left is duplicate, keep going
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                continue

            if two_sum < target:
                left += 1
                continue

            if two_sum > target:
                right -= 1
                continue

        return pairs