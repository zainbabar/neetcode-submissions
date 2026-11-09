class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # if theres only 1 num between left and right
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # didnt find it, right is < left now by 1
        # right is now the index value just before 
        # left is now index of value just after
        # so if it appeared, it would appear in between these two
        return left