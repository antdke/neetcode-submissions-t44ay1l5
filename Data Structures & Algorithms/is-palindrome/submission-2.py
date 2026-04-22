class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Option 1
        # Traverse string and remove non-alpha chars
        # Reverse string
        # Check if reversed and normal equal

        # Inefficient because of reversing algorithm

        # Option 2
        # Use 2 pointers to check front and back of string
        # Loop until they meet in the middle
        # Skip non-alpha chars
        # If at any point the chars don't match, return False
        # Else return True

        left = 0
        right = len(s) - 1

        while left < right:
            
            # check if left is not alpha-num, if so increment
            if not s[left].isalnum():
                left += 1
                continue

            # check if right is not alpha-num, if so decrement
            if not s[right].isalnum():
                right -= 1
                continue

            # if both are alpha-num, check if lowered not equal -> return False
            if s[left].lower() != s[right].lower():
                return False

            # move both pointers
            left += 1
            right -= 1

        # return True
        return True