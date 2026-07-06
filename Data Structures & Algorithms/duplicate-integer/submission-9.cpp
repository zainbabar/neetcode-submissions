class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (auto el: nums) seen.insert(el);
        return seen.size() != nums.size();
    }
};