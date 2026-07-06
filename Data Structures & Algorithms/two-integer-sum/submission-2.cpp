class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> nums_map;
        for (int i = 0; i < nums.size(); ++i) { nums_map.insert({nums[i], i}); }
        for (int i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];
            if (nums_map.contains(diff) && nums_map[diff] != i) return nums_map[diff] < i ? vector<int>{nums_map[diff], i} : vector<int>{i, nums_map[diff]};
        }
        return nums;
    }
};
