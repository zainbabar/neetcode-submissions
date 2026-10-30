from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        # buckets[c] holds every number that shows up exactly c times
        # a number can show up at most len(nums) times, so we need len(nums) + 1 buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        # walk from the highest count down until we have at least k numbers
        output = []
        for bucket in reversed(buckets):
            output += bucket
            if len(output) >= k:
                break
        return output[:k]