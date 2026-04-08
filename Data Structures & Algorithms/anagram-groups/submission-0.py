class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create defaultdict of type list
        # for each s in strs
            # create list of 26 0s for each char in alphabet
            # for each char in s, increment the index for that char
            # convert that list into a tuple
            # store that s into default dict at the list of that tuple key
        # return list defaultdict.values

        anagrams_map = collections.defaultdict(list)

        for s in strs:
            s_chars = [0] * 26
            for char in s:
                s_chars[ord(char) - ord('a')] += 1
            anagrams_map[tuple(s_chars)].append(s)

        return list(anagrams_map.values())