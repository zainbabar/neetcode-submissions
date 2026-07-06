class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> seen1;
        unordered_map<char, int> seen2;
        for (auto el: s) { ++seen1[el]; }
        for (auto el: t) { ++seen2[el]; }
        for (auto el: s) {
            if (seen2[el] != seen1[el]) return false;
        }
        for (auto el: t) {
            if (seen1[el] != seen2[el]) return false;
        }
        return true;
    }
};
