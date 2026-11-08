class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - (nums[i])
            left = i + 1 
            right = len(nums) - 1
            while left < right: # j and k
                val = nums[left] + nums[right]
                if val == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # keep moving left/right past any duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif val < target: # too small, move left to bigger. num
                    left += 1
                else:
                    right -= 1
        return output

