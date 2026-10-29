class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # walk thru array once, keep a dict of values we have alr seen
        # and see if target - x is in it 

        # basically see based on the current number we are on 
        # waht is the matching number that would add up to the target
        # and have we already seen it
        seen = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in seen and seen[x] != i:
                return [seen[x], i]
            seen[nums[i]] = i
            

    
        
