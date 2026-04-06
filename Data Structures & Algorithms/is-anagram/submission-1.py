class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # hashmap for s
        # hashmap for t
        # iterate and count elements of s
        # same for t
        # compare hashmap values

        map_s = {}
        map_t = {}

        for index, char in enumerate(s):

            if char in map_s:
                map_s[char] += 1
                continue

            map_s[char] = 1

        for index, char in enumerate(t):

            if char in map_t:
                map_t[char] += 1
                continue

            map_t[char] = 1

        return map_s == map_t
        