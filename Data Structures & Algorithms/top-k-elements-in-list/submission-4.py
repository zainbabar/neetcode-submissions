from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        top_k = heapq.nlargest(k, counts, key=counts.get)
        # have the k largest counts
        # now we just need to get the k elements with these counts
        return top_k

