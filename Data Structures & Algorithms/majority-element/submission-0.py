from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thres = len(nums) // 2
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] > thres:
                return num