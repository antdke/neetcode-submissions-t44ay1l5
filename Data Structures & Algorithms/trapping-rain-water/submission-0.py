class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
    
        total_rain_water = 0

        left_max = 0
        right_max = 0

        while left < right:

            if height[left] < height[right]:

                left_max = max(left_max, height[left])
                total_rain_water += left_max - height[left]
                left += 1

            else:

                right_max = max(right_max, height[right])
                total_rain_water += right_max - height[right]
                right -= 1
        
        return total_rain_water