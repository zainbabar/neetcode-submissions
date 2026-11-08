class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # since its sorted, all duplicate elements are adjacent
        p1 = 1
        p2 = 1
        n = len(nums)
        while p2 < n:
            # identical elements, move the read ptr forward
            if nums[p2] == nums[p1 - 1]:
                p2 += 1

            # found two elements that are not the same 
            # move the write ptr forward, write into this new slot
            # we know this new slot is either a duplicate 
            # or the first new number (where read is) so it would be a no op
            else:
                nums[p1] = nums[p2]
                p1 += 1 # move the write ptr forward, this is now a unique slot
                p2 += 1
        
        return p1



