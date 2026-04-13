class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create map for frequency
        # freq count array

        freq_map = collections.defaultdict(int)
        count_array = [[] for _ in range(len(nums) + 1)]

        # count frequencies in map
        for num in nums:
            freq_map[num] += 1

        # bucket sort frequences into count_array
        for num, count in freq_map.items():
            count_array[count].append(num)

        # pop k results into result array
        res = []
        for index in range(len(count_array) - 1, 0, -1):

            if len(count_array[index]) == 0:
                continue

            
            for num in count_array[index]:
                res.append(num)
                if len(res) == k:
                    return res
            