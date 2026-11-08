class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = {}
        for num in nums:
            seen[num] = True
        
        # build out our possible starting positons 
        # and the longest consecutive we can build for each starting 
        starts = set()
        for num in nums:
            # start of the sequence, number after but nothing before
            if seen.get(num+1) is not None and seen.get(num-1) is None:
                starts.add(num)

        max_len = 1
        cur_len = 1
        for num in starts:
            while seen.get(num + 1) is not None:
                cur_len += 1
                num += 1
            max_len = max(max_len, cur_len)
            cur_len = 1
        
        return max_len


