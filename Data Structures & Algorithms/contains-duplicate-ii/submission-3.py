class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window of size k, see if. any duplicates in this window
        left = 0
        seen = set()
        for i in range(len(nums)):
            if len(seen) > k:
                seen.remove(nums[left])
                left += 1
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False


