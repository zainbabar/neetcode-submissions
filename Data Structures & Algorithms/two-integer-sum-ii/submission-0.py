class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1 
        output = []
        # invariant that left != right, left & right correspond to index1 n 2 respectively
        while left < right: 
            val = numbers[left] + numbers[right]
            # our computed value is too big so we should the right ptr
            # to get a smaller value 
            if val > target:
                right -= 1
            # val is too small, move the left ptr to get a bigger value
            elif val < target:
                left += 1
            else: # match
                output = [left + 1, right + 1]
                break

        return output
