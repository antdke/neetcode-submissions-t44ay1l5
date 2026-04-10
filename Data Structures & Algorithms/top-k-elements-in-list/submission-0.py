class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a map
        # traverse array to grab the existence and freq of nums
        # sort map by freq count
        # grab top k

        freq_map = collections.defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        freq_map_sorted = dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True))

        print(freq_map_sorted)
        print(list(freq_map_sorted.keys())[:2])

        return list(freq_map_sorted.keys())[:k]



