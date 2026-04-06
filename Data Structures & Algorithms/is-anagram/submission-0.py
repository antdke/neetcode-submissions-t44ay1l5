class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sort first
        # iterate through both string at the same time
        # check if values match at each step

        # hashmap for s
        # hashmap for t
        # iterate and count elements of s
        # same for t
        # compare hashmap values

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        print(sorted_s)
        print(sorted_t)

        if len(s) != len(t):
            return False

        for n in range(len(s)):
            
            if sorted_s[n] != sorted_t[n]:
                return False

        return True

        