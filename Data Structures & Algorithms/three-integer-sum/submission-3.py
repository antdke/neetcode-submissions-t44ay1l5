class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # create triplets array
        # sort nums
        # enumerate nums
        # if current num is > 0, return triplets
        # if current index is not 0 and current num is the same as the num before it, continue
        # create empty twoSumPairs array
        # store self.twoSum(num * -1, index, nums)
        # for pair in twoSumPairs
            # append num to each pair
            # store each pair in triplets
        # return triplets

        triplets = []
        nums.sort()
        print(nums)
        for index, num in enumerate(nums):

            if num > 0:
                return triplets

            if index > 0 and num == nums[index - 1]:
                continue

            two_sum_pairs = []

            two_sum_pairs = self.twoSum(num * -1, index + 1, nums)
            print(two_sum_pairs)
            print("NUM")
            print(num)
            for pair in two_sum_pairs:
                pair.append(num)
                triplets.append(pair)

        return triplets


        # twoSum (self, target, index, nums)
        # create twoSumPair array
        # left is index
        # right is len(nums) - 1
        # target is negative of current num in nums
        # while left < right
            # if twoSum is equal target, 
                # append found pair to twoSumPair array
                # increment left
                # while left < right and nums[left] == nums[left - 1]
                    # increment left
            # if twoSum is less than target, increment left
            # if twoSum is more than target, decrement right
        # return twoSumPair

    def twoSum(self, target, index, nums):

        two_sum_pairs = []
        left = index
        right = len(nums) - 1

        print(target)
        print(left)
        print(right)

        while left < right:
            
            two_sum = nums[left] + nums[right]

            if two_sum == target:
                
                two_sum_pairs.append([nums[left], nums[right]])
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                continue

            if two_sum < target:
                left += 1
                continue

            if two_sum > target:
                right -= 1
                continue

            
        return two_sum_pairs

            