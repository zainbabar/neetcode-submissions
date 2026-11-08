class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, keep increasing the size of the window
        max_len = 0
        indicies = {}
        substr = ""
        left = 0
        for i in range(len(s)):
            # duplicate char hasnt arrivfed yet
            # add our new char to the substr, move our wrindow right
            # save its index for later if we need to chop
            if s[i] not in substr:
                substr += s[i]
                indicies[s[i]] = i
                max_len = max(max_len, len(substr))
            # we have a duplicate char
            # instead of throwing away the entire substr
            # chop out the duplicate and everything before
            else:
                left = indicies[s[i]] + 1
                indicies[s[i]] = i
                substr = s[left:i+1]
                max_len = max(max_len, len(substr))

        return max_len



