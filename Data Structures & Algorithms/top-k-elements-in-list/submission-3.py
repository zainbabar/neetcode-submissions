from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        heapq.heapify(list(counts.values()))
        top_k = heapq.nlargest(k, list(counts.values()))
        # have the k largest counts
        # now we just need to get the k elements with these counts
        output = []
        for num, count in counts.items():
            if count in top_k:
                output.append(num)
        return output
