class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        total_rain_water = 0
        left_max_height = 0
        right_max_height = 0

        while left < right:

            if height[left] < height[right]:

                left_max_height = max(height[left], left_max_height)
                total_rain_water += left_max_height - height[left]
                left += 1

            else:

                right_max_height = max(height[right], right_max_height)
                total_rain_water += right_max_height - height[right]
                right -= 1

        return total_rain_water

