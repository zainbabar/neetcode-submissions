class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        output = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            target = 0 - (nums[i])
            left = i + 1 
            right = len(nums) - 1
            left_visited = set()
            right_visited = set()
            while left < right: # j and k
                if nums[left] in left_visited:
                    left += 1
                    continue
                if nums[right] in right_visited:
                    right -= 1
                    continue
                val = nums[left] + nums[right]
                if val == target:
                    output.append([nums[i], nums[left], nums[right]])
                    right_visited.add(nums[right])
                    left_visited.add(nums[left])
                    left += 1
                    right -= 1
                elif val < target: # too small, move left to bigger. num
                    left += 1
                else:
                    right -= 1
        return output

