class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Option 1
        # Create a map to hold last index of a seen char
        # Left/right pointers that slide together as a window
        # Longest length result var
        # Traverse the string
        # Increment the right pointer of the window
        # Keep track of when we last saw a char using the index
        # Save the longest length using max()
        # Slide left side of window upon seeing duplicate from right side
        # Slide it one over from where we last saw the duplicate (only if it's ahead)

        most_recent_index = {}
        left = 0
        longest_length = 0

        for right in range(len(s)):

            if s[right] in most_recent_index:
                left = max(left, most_recent_index[s[right]] + 1)

            most_recent_index[s[right]] = right
            longest_length = max(right - left + 1, longest_length)

        return longest_length
