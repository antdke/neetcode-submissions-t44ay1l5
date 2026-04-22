class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Bucket Sort

        # count frequencies in hashmap

        # bucket numbers into frequencies using array indices as counts
        # store the numbers as arrays in each index

        # traverse the top k buckets and pop from greatest to lowest until k

        freq_map = collections.defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        top_k_bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq_map.items():
            top_k_bucket[count].append(num)

        res = []

        for index in range(len(top_k_bucket) - 1, 0, -1):
            while len(top_k_bucket[index]) > 0:
                res.append(top_k_bucket[index].pop())
                if len(res) == k:
                    return res
