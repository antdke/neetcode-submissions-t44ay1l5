class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Area = height + width
        # Widest with is first and last index
        # We work our way in, checking/storing heights before each move 
        # Change index based on which is shorter height
        # If same height move both b/c shorter one will be constraint

        # left/right pointers
        # max_water = 0
        # while left < right
            # if height_left < height_right

                # get current water -> (min height) * (diff btwn right/left)
                # get max water -> max(max_water, current_water)
                # increment left

            # elseif height_right < height_left

                # get current water -> (min height) * (diff btwn right/left)
                # get max water -> max(max_water, current_water)
                # decrement right

            # else

                # get current water -> (min height) * (diff btwn right/left)
                # get max water -> max(max_water, current_water)
                # increment left
                # decrement right

        left = 0
        right = len(heights) - 1

        max_water = 0
        current_water = 0

        while left < right:

            if heights[left] < heights[right]:

                current_water = min(heights[left], heights[right]) * (right - left)
                max_water = max(max_water, current_water)
                left += 1

            elif heights[right] < heights[left]:

                current_water = min(heights[left], heights[right]) * (right - left)
                max_water = max(max_water, current_water)
                right -= 1

            else:

                current_water = min(heights[left], heights[right]) * (right - left)
                max_water = max(max_water, current_water)
                left += 1
                right -= 1

        return max_water