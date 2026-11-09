class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # target wasnt found  so left and right have crossed
        # right = left - 1
        # all elements before left are smaller than target
        # all elements at or after left are larger than target
        # so left is where target should be inserted
        return left