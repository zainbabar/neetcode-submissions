class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int>seen;
        for (auto elem: nums) {
            seen.insert(elem);
        }
        return seen.size() != nums.size();
    }
};