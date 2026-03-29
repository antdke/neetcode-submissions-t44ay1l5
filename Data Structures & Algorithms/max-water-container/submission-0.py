class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:

            current_water = min(heights[left], heights[right]) * (right - left)
            max_water = max(max_water, current_water)
            
            if heights[left] < heights[right]:
                left += 1
                continue
            
            if heights[right] < heights[left]:
                right -= 1
                continue

            left += 1
            right -= 1

        return max_water