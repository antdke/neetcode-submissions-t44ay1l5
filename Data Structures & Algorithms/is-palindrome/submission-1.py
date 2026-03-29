class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # start at both ends
        # work inwards
        # if left not at alphanum, increment left by 1
        # if right not at alphanum, decrement right by 1
        # once both at alphanum, check if equal
        # if not, return False
        # continue while left is less than right
        # return True on end condition

        left = 0
        right = len(s) - 1

        while left < right:
            
            if s[left].isalnum() == False:
                left += 1
                continue

            if s[right].isalnum() == False:
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True