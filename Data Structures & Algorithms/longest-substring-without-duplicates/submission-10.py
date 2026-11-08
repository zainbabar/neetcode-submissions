class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, keep increasing the size of the window
        max_len = 0
        indicies = {}
        left = 0
        for i in range(len(s)):
            # have not seen this char before
            if indicies.get(s[i]) is None:
                indicies[s[i]] = i
            # have seen this char before, update our window if it is inside
            else:
                # if the old copy was within the window then move
                # if it wasnt then its fine leave the windwo
                left = max(indicies[s[i]] + 1, left)
                indicies[s[i]] = i
            max_len = max(max_len, (i - left) + 1)

        return max_len



