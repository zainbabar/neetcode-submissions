from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        # indexed by count, ex if 3 has count 2
        # list_counts[2] == 3 
        # then just get the k most frequent elements
        # use a list if multiple nubmers have the same count
        list_counts = [[] for _ in range(len(nums) + 1)]
        for num in counts:
            list_counts[counts[num]].append(num)
        
        output = []
        for counts in reversed(list_counts):
            delta = k - len(output)
            if delta <= 0:
                break
            if len(counts) <= delta:
                output = output + counts
            else:
                output = output + counts[delta:]
        
        return output
        
            